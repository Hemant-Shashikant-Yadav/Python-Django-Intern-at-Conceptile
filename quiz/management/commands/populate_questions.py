from django.core.management.base import BaseCommand
from quiz.models import Question

class Command(BaseCommand):
    help = 'Populate quiz questions'

    def handle(self, *args, **kwargs):
        Question.objects.all().delete()

        questions = [
            {
                'text': 'What is the capital of France?',
                'option_a': 'London',
                'option_b': 'Berlin', 
                'option_c': 'Paris',
                'option_d': 'Madrid',
                'correct_answer': 'C'
            },
            {
                'text': 'Which planet is known as the Red Planet?',
                'option_a': 'Venus',
                'option_b': 'Mars',
                'option_c': 'Jupiter',
                'option_d': 'Saturn',
                'correct_answer': 'B'
            },
            {
                'text': 'What is the largest mammal in the world?',
                'option_a': 'Elephant',
                'option_b': 'Giraffe',
                'option_c': 'Blue Whale',
                'option_d': 'Hippopotamus',
                'correct_answer': 'C'
            },
            {
                'text': 'Who painted the Mona Lisa?',
                'option_a': 'Vincent Van Gogh',
                'option_b': 'Pablo Picasso',
                'option_c': 'Leonardo da Vinci',
                'option_d': 'Michelangelo',
                'correct_answer': 'C'
            },
            {
                'text': 'What is the chemical symbol for gold?',
                'option_a': 'Ag',
                'option_b': 'Au',
                'option_c': 'Fe',
                'option_d': 'Cu',
                'correct_answer': 'B'
            },
            {
                'text': 'Which country is home to the Great Barrier Reef?',
                'option_a': 'Brazil',
                'option_b': 'Indonesia',
                'option_c': 'Australia',
                'option_d': 'Mexico',
                'correct_answer': 'C'
            },
            {
                'text': 'What is the largest organ in the human body?',
                'option_a': 'Liver',
                'option_b': 'Brain',
                'option_c': 'Heart',
                'option_d': 'Skin',
                'correct_answer': 'D'
            },
            {
                'text': 'Which programming language is known as the "mother of all languages"?',
                'option_a': 'Java',
                'option_b': 'C',
                'option_c': 'Python',
                'option_d': 'JavaScript',
                'correct_answer': 'B'
            },
            {
                'text': 'What is the capital of Japan?',
                'option_a': 'Seoul',
                'option_b': 'Beijing',
                'option_c': 'Tokyo',
                'option_d': 'Bangkok',
                'correct_answer': 'C'
            },
            {
                'text': 'Which element has the atomic number 1?',
                'option_a': 'Helium',
                'option_b': 'Oxygen',
                'option_c': 'Hydrogen',
                'option_d': 'Carbon',
                'correct_answer': 'C'
            },
            {
                'text': 'Who wrote "Romeo and Juliet"?',
                'option_a': 'Charles Dickens',
                'option_b': 'William Shakespeare',
                'option_c': 'Jane Austen',
                'option_d': 'Mark Twain',
                'correct_answer': 'B'
            },
            {
                'text': 'What is the largest desert in the world?',
                'option_a': 'Gobi Desert',
                'option_b': 'Sahara Desert',
                'option_c': 'Arabian Desert',
                'option_d': 'Antarctica',
                'correct_answer': 'D'
            },
            {
                'text': 'Which continent is the driest?',
                'option_a': 'Africa',
                'option_b': 'Australia',
                'option_c': 'Antarctica',
                'option_d': 'Asia',
                'correct_answer': 'C'
            },
            {
                'text': 'What is the speed of light?',
                'option_a': '299,792 kilometers per second',
                'option_b': '150,000 kilometers per second',
                'option_c': '200,000 kilometers per second',
                'option_d': '350,000 kilometers per second',
                'correct_answer': 'A'
            },
            {
                'text': 'Who developed the theory of relativity?',
                'option_a': 'Isaac Newton',
                'option_b': 'Nikola Tesla',
                'option_c': 'Albert Einstein',
                'option_d': 'Stephen Hawking',
                'correct_answer': 'C'
            },
            {
                'text': 'What is the largest organ in the human body?',
                'option_a': 'Liver',
                'option_b': 'Brain',
                'option_c': 'Heart',
                'option_d': 'Skin',
                'correct_answer': 'D'
            },
            {
                'text': 'Which river is the longest in the world?',
                'option_a': 'Amazon River',
                'option_b': 'Nile River',
                'option_c': 'Mississippi River',
                'option_d': 'Yangtze River',
                'correct_answer': 'B'
            },
            {
                'text': 'What is the smallest prime number?',
                'option_a': '0',
                'option_b': '1',
                'option_c': '2',
                'option_d': '3',
                'correct_answer': 'C'
            },
            {
                'text': 'Which mountain is the tallest in the world?',
                'option_a': 'K2',
                'option_b': 'Mount Everest',
                'option_c': 'Kangchenjunga',
                'option_d': 'Makalu',
                'correct_answer': 'B'
            },
            {
                'text': 'What is the main component of the Sun?',
                'option_a': 'Helium',
                'option_b': 'Hydrogen',
                'option_c': 'Oxygen',
                'option_d': 'Carbon',
                'correct_answer': 'B'
            },
            {
                'text': 'Who invented the telephone?',
                'option_a': 'Thomas Edison',
                'option_b': 'Nikola Tesla',
                'option_c': 'Alexander Graham Bell',
                'option_d': 'Guglielmo Marconi',
                'correct_answer': 'C'
            },
            {
                'text': 'What is the chemical symbol for Silver?',
                'option_a': 'Si',
                'option_b': 'Ag',
                'option_c': 'Au',
                'option_d': 'Fe',
                'correct_answer': 'B'
            },
            {
                'text': 'Which programming language is known for web development?',
                'option_a': 'Java',
                'option_b': 'C++',
                'option_c': 'Python',
                'option_d': 'JavaScript',
                'correct_answer': 'D'
            },
            {
                'text': 'What is the largest planet in our solar system?',
                'option_a': 'Saturn',
                'option_b': 'Neptune',
                'option_c': 'Jupiter',
                'option_d': 'Uranus',
                'correct_answer': 'C'
            },
            {
                'text': 'Who wrote "1984"?',
                'option_a': 'Aldous Huxley',
                'option_b': 'George Orwell',
                'option_c': 'Ray Bradbury',
                'option_d': 'Franz Kafka',
                'correct_answer': 'B'
            },
            {
                'text': 'What is the hardest natural substance on Earth?',
                'option_a': 'Gold',
                'option_b': 'Platinum',
                'option_c': 'Diamond',
                'option_d': 'Steel',
                'correct_answer': 'C'
            },
            {
                'text': 'Which country is the largest by land area?',
                'option_a': 'Canada',
                'option_b': 'United States',
                'option_c': 'China',
                'option_d': 'Russia',
                'correct_answer': 'D'
            },
            {
                'text': 'What is the main language spoken in Brazil?',
                'option_a': 'Spanish',
                'option_b': 'Portuguese',
                'option_c': 'Italian',
                'option_d': 'French',
                'correct_answer': 'B'
            },
            {
                'text': 'Who painted "Starry Night"?',
                'option_a': 'Claude Monet',
                'option_b': 'Pablo Picasso',
                'option_c': 'Vincent Van Gogh',
                'option_d': 'Salvador Dali',
                'correct_answer': 'C'
            },
            {
                'text': 'What is the main ingredient in traditional Japanese miso soup?',
                'option_a': 'Tofu',
                'option_b': 'Seaweed',
                'option_c': 'Fermented soybean paste',
                'option_d': 'Rice',
                'correct_answer': 'C'
            }
        ]

        for q in questions:
            Question.objects.create(**q)
        
        self.stdout.write(self.style.SUCCESS('Successfully populated 30 questions'))