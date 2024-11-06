import random
from data.word_lists import (
    ADJECTIVES, CREATURES, HABITATS, PREPOSITIONS,
    FAMOUS_SCIENTISTS, HISTORICAL_FIGURES, CELEBRITIES, POLITICIANS,
    OBJECTS, APPLIANCES, APPAREL,
    PLANETS, COUNTRIES, FAMOUS_PLACES, HISTORICAL_PLACES
)

class PhraseGenerator:
    def generate_phrase(self) -> str:
        """Generate a random phrase with 1-3 words from various categories."""
        category = random.choice(['animals', 'humans', 'things', 'places'])
        
        if category == 'animals':
            return self._generate_animal_phrase()
        elif category == 'humans':
            return self._generate_human_phrase()
        elif category == 'things':
            return self._generate_thing_phrase()
        else:  # places
            return self._generate_place_phrase()

    def _generate_animal_phrase(self) -> str:
        """Generate a random animal phrase with 1-3 words."""
        num_words = random.randint(1, 3)
        
        if num_words == 1:
            return random.choice(CREATURES)
        elif num_words == 2:
            return f"{random.choice(ADJECTIVES)} {random.choice(CREATURES)}"
        else:
            return f"{random.choice(ADJECTIVES)} {random.choice(CREATURES)} {random.choice(PREPOSITIONS)} {random.choice(HABITATS)}"

    def _generate_human_phrase(self) -> str:
        """Generate a random human phrase with 1-2 words."""
        human_categories = [FAMOUS_SCIENTISTS, HISTORICAL_FIGURES, CELEBRITIES, POLITICIANS]
        category = random.choice(human_categories)
        
        if random.choice([True, False]):
            return f"{random.choice(ADJECTIVES)} {random.choice(category)}"
        else:
            return random.choice(category)

    def _generate_thing_phrase(self) -> str:
        """Generate a random thing phrase with 1-2 words."""
        thing_categories = [OBJECTS, APPLIANCES, APPAREL]
        category = random.choice(thing_categories)
        
        if random.choice([True, False]):
            return f"{random.choice(ADJECTIVES)} {random.choice(category)}"
        else:
            return random.choice(category)

    def _generate_place_phrase(self) -> str:
        """Generate a random place phrase with 1-3 words."""
        place_categories = [PLANETS, COUNTRIES, FAMOUS_PLACES, HISTORICAL_PLACES]
        category = random.choice(place_categories)
        
        num_words = random.randint(1, 3)
        
        if num_words == 1:
            return random.choice(category)
        elif num_words == 2:
            return f"{random.choice(ADJECTIVES)} {random.choice(category)}"
        else:
            return f"{random.choice(ADJECTIVES)} {random.choice(category)} {random.choice(PREPOSITIONS)} {random.choice(HABITATS)}"