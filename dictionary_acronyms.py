acronyms={"LOL":"laugh out loud", "IDK":"I do not know","TBH": "to be hones"}

sentence="IDK" + " what happened " + "TBH"
translation=acronyms.get("IDK") + " what happened"+ acronyms.get("TBH")
print("sentence:", sentence)
print("translation", translation)
