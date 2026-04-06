import json
import urllib.error
import urllib.request

from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from Pokedex.models import Pokemon


def _fetch_json(url: str, timeout: int = 20) -> dict:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "pokedex_projectv1/1.0 (Django seed command)",
            "Accept": "application/json",
        },
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def _stat(stats: list[dict], name: str) -> int:
    for s in stats:
        if s.get("stat", {}).get("name") == name:
            return int(s.get("base_stat", 0))
    return 0


class Command(BaseCommand):
    help = "Fetch Pokemon data from PokeAPI and populate the local database."

    def add_arguments(self, parser):
        parser.add_argument("--start", type=int, default=1, help="Start Pokemon ID (default: 1)")
        parser.add_argument("--limit", type=int, default=251, help="How many Pokemon to fetch (default: 251)")
        parser.add_argument(
            "--clear",
            action="store_true",
            help="Delete existing Pokemon rows before seeding",
        )

    def handle(self, *args, **options):
        start: int = options["start"]
        limit: int = options["limit"]
        clear: bool = options["clear"]

        if start < 1:
            raise CommandError("--start must be >= 1")
        if limit < 1:
            raise CommandError("--limit must be >= 1")

        end = start + limit - 1

        if clear:
            deleted, _ = Pokemon.objects.all().delete()
            self.stdout.write(self.style.WARNING(f"Cleared {deleted} Pokemon rows."))

        created = 0
        updated = 0
        failed = 0

        for pokemon_id in range(start, end + 1):
            url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
            try:
                data = _fetch_json(url)
            except (urllib.error.URLError, TimeoutError) as e:
                failed += 1
                self.stderr.write(self.style.ERROR(f"[{pokemon_id}] fetch failed: {e}"))
                continue

            payload = {
                "name": str(data.get("name", "")).capitalize(),
                "image_url": (
                    (data.get("sprites", {}) or {})
                    .get("other", {})
                    .get("official-artwork", {})
                    .get("front_default")
                )
                or "",
                "height": int(data.get("height", 0) or 0),
                "weight": int(data.get("weight", 0) or 0),
                "hp": _stat(data.get("stats", []) or [], "hp"),
                "attack": _stat(data.get("stats", []) or [], "attack"),
                "defense": _stat(data.get("stats", []) or [], "defense"),
                "special_attack": _stat(data.get("stats", []) or [], "special-attack"),
                "special_defense": _stat(data.get("stats", []) or [], "special-defense"),
                "speed": _stat(data.get("stats", []) or [], "speed"),
            }

            with transaction.atomic():
                obj, was_created = Pokemon.objects.update_or_create(id=pokemon_id, defaults=payload)

            if was_created:
                created += 1
            else:
                updated += 1

            if pokemon_id == start or pokemon_id % 25 == 0 or pokemon_id == end:
                self.stdout.write(f"Seeded up to ID {pokemon_id}...")

        self.stdout.write(
            self.style.SUCCESS(
                f"Done. created={created} updated={updated} failed={failed} total_now={Pokemon.objects.count()}"
            )
        )
