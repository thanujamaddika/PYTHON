from textblob import TextBlob
import language_tool_python  # Corrected import

class SpellCheckerModule:
    def __init__(self):  # Fixed constructor name
        self.spell_check = TextBlob("")
        self.grammar_tool = language_tool_python.LanguageTool('en-US')  # Fixed grammar checker

    def correct_spell(self, text):
        words = text.split()
        corrected_words = [str(TextBlob(word).correct()) for word in words]
        return " ".join(corrected_words)

    def correct_grammar(self, text):
        matches = self.grammar_tool.check(text)  # Using language_tool_python
        corrections = [match.message for match in matches]
        return corrections, len(corrections)

if __name__ == "__main__":  # Fixed the syntax
    obj = SpellCheckerModule()
    message = "Hello world. I like mashine learning. appple. bananana"
    print("Corrected Spelling:", obj.correct_spell(message))
    print("Grammar Errors:", obj.correct_grammar(message))
