# About

This project enables the user to easily develop challenges in [challenges](InscryptionSaveManager/src/challenges.py). These challenges are used in [main_scrypt](InscryptionSaveManager/src/main_scrypt.py). Challenges can be combined, as each challenge is a child class of the Challenge class. A ChallengeManager object is instantiated in main_scrypt with a list of challenges. So, one could play a run that clamps attack stat to 2 and adds a beehive on every save. That would be weird. Funny.

# Use

To use this project, install the necessary packages with

    pipenv install
  
Then execute the main script with

    pipenv run py InscryptionSaveManager/src/main_scrypt.py

# Adding challenges

To create a new challenge, begin with a child class of the Challenge object.

```python
class NewChallenge(Challenge):

    def __init__(self, meta_logger: ProjectLogger, ui_logger: ProjectLogger) -> None:
        super().__init__(meta_logger, ui_logger)
    
    def startup_query(self) -> None:
        return super().startup_query()
    
    def run(self, cards: list[Card]) -> bool:
        return super().run(cards)
```

Modify the run method by deleting 'return '. Then add the challenge logic and return a bool if this challenge requires that the project should write the new list of cards to the save file.

Here's an example that names every card "Doctor " and then the typical name of the card.

```python
class DoctorRenamer(Challenge):

    def __init__(self, meta_logger: ProjectLogger, ui_logger: ProjectLogger) -> None:
        super().__init__(meta_logger, ui_logger)
    
    def startup_query(self) -> None:
        return super().startup_query()
    
    def run(self, cards: list[Card]) -> bool:
        super().run(cards)

        write_necessary = False

        # Iterate through all cards
        for card in cards:
            
            # Check to see if this card needs to have 'Doctor' added to its name
            this_card_doctor_named = False

            # Look through each parsed mod config object
            for mod_config in card.mod_configs:

                # Check if there's a mod config that already names this card 'Doctor '
                if mod_config.replacement_name.startswith("Doctor"):
                    this_card_doctor_named = True

            # Uh oh! This card isn't named doctor.
            # We'll create a new mod config for that.
            if not this_card_doctor_named:

                self.meta_logger.log(level= INFO, message= f"Card {card.creature.name} is missing 'Doctor'!")

                write_necessary = True # The whole deck will need to be written

                new_mod_config = CardModConfig()
                new_mod_config.replacement_name = "Doctor " + card.base_stats.display_name

                # Add that mod config to the card
                card.add_mod_config(new_mod_config)
        
        return write_necessary
```

This works if we run it.

![doctor_cards](_readme_docs/doctor_rename_cards.png)

# Logging

There are two log files: meta_logger and ui_logger. Typically, use ui_logger to display text to the user. It doesn't have a timestamp or anything like that- it's basically a replacement for print() so that you can look back through a log of user displayed messages. meta_logger is for more detailed debugging.

