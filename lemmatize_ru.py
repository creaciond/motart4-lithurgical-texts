from pymystem3 import Mystem
import os


mystem = Mystem()
if not os.path.exists("./ru_lemmas"):
    os.mkdir("./ru_lemmas")

for filename in os.listdir("./ru_orig"):
    if filename.endswith(".txt"):
        lems = []
        with open("./ru_orig/"+filename, "r", encoding="utf-8") as f:
            text = [line for line in f.readlines() if not line.startswith("#")]
            for line in text:
                analyses = mystem.analyze(line)
                lemmas = " ".join([parse["analysis"][0]["lex"] for parse in analyses if parse.get("analysis")])
                lems.append(lemmas)
        ready_lemmas = "\n".join(lems)
        with open("./ru_lemmas/"+filename, "w", encoding="utf-8") as f:
            f.write(ready_lemmas)