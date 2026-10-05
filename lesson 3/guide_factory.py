from dataclasses import make_dataclass


GuideEntry = make_dataclass(
    "GuideEntry",
    [
        ("planet", str),
        ("entry", str),
        ("danger_level", int, 0),
    ],
)


magrathea = GuideEntry(
    planet="Магратея",
    entry="Планета, созданная специально для строительства...",
    danger_level=10,
)
