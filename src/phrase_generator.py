import random
from data.word_lists import (
    ADJECTIVES, CREATURES, HABITATS, PREPOSITIONS,
    FAMOUS_SCIENTISTS, HISTORICAL_FIGURES, CELEBRITIES, POLITICIANS,
    OBJECTS, APPLIANCES, APPAREL,
    PLANETS, COUNTRIES, FAMOUS_PLACES, HISTORICAL_PLACES,
    WHAT_QUESTIONS, WHY_QUESTIONS, WHEN_QUESTIONS,
    WHO_QUESTIONS, WHERE_QUESTIONS, HOW_QUESTIONS
)

class PhraseGenerator:
    def generate_phrase(self) -> str:
        """Generate a random phrase with 1-3 words from various categories."""
        category = random.choice(['animals', 'humans', 'things', 'places', 'questions'])
        
        if category == 'animals':
            return self._generate_animal_phrase()
        elif category == 'humans':
            return self._generate_human_phrase()
        elif category == 'things':
            return self._generate_thing_phrase()
        elif category == 'questions':
            return self._generate_question_phrase()
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
            
    def _generate_question_phrase(self) -> str:
        """Generate a random question using the 5W1H format."""
        # Select a question type (What, Why, When, Who, Where, How)
        question_type = random.choice([
            WHAT_QUESTIONS, WHY_QUESTIONS, WHEN_QUESTIONS, 
            WHO_QUESTIONS, WHERE_QUESTIONS, HOW_QUESTIONS
        ])
        
        # Select a random question template from the chosen type
        question_template = random.choice(question_type)
        
        # Determine what kind of subject(s) to use in the question
        if "{}" in question_template:
            # For templates with one placeholder
            if question_template.count("{}") == 1:
                # Choose a random category for the subject
                subject_category = random.choice([
                    CREATURES, 
                    FAMOUS_SCIENTISTS, HISTORICAL_FIGURES, CELEBRITIES, POLITICIANS,
                    OBJECTS, APPLIANCES, APPAREL,
                    PLANETS, COUNTRIES, FAMOUS_PLACES, HISTORICAL_PLACES
                ])
                
                # Select a random item from the chosen category
                subject = random.choice(subject_category)
                
                # Apply optional adjective (50% chance)
                if random.random() > 0.5:
                    subject = f"{random.choice(ADJECTIVES)} {subject}"
                    
                # Format the question with the subject
                return question_template.format(subject)
                
            # For templates with two placeholders (comparisons)
            elif question_template.count("{}") == 2:
                # Choose a random category for both subjects
                subject_category = random.choice([
                    CREATURES, 
                    FAMOUS_SCIENTISTS, HISTORICAL_FIGURES, CELEBRITIES, POLITICIANS,
                    OBJECTS, APPLIANCES, APPAREL,
                    PLANETS, COUNTRIES, FAMOUS_PLACES, HISTORICAL_PLACES
                ])
                
                # Select two different items from the chosen category
                subject1 = random.choice(subject_category)
                subject2 = random.choice([s for s in subject_category if s != subject1])
                
                # Format the question with both subjects
                return question_template.format(subject1, subject2)
        
        # Fallback in case template parsing failed
        return "What is the meaning of life?"