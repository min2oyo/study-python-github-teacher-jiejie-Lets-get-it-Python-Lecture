import operator

alibaba = "in a town of persia lived two brothers , sons of a poor man , one named cassim , the other alibaba . cassim , the elder , married a wife with a considerable fortune , and lived at his ease , but the wife of alibaba was as poor as himself . they dwelt in a mean cottage in the suburbs , and he maintained his family by cutting wood . alibaba was in the forest preparing to load his asses with the faggots he had cut , when he saw a troop of horsemen approaching . he hastily climbed a large thick tree , and hid himself among the branches . alibaba counted forty of them , each took a loaded portmanteau from his horse , and turning to the rock , said , open , sesame immediately a door opened , the robbers passed in , when the door shut of itself . in a short time the door opened again , and the robbers came out , who said , shut , sesame . the door instantly closed . alibaba ventured down , and approaching the rock , said , open , sesame . immediately the door flew open . he brought his asses , and took as many bags of gold coin as they could carry . alibaba told his brother the secret of the cave . cassim rose early next morning , and set out with ten mules loaded with great chests . he found the rock , and having said , open sesame , gained admission , where he found more treasures than he expected , which made him forget the word that caused the door to open . presently he heard the sound of horses feet , which he concluded to be the robbers , who instantly put him to death . alibaba drove to the forest , and on entering the cave , he found the body of his brother cut into quarters . he took the quarters , and put them upon one of his asses , and delivered the body to cassim wife . morgiana , a female slave in his brother house , was sent early next morning to a poor cobbler , and gave him two pieces of gold to go with her blindfolded , taking him into the room where the body was lying , bade him sew the mangled limbs together . mustapha obeyed , having received two pieces of gold , and was led blindfolded the same way back . cassim was buried with all due solemnity , and alibaba removed to the house of his deceased brother , of which he took possession . the captain of the troop resolved to find out who possessed the secret of entrance into his cave , and disguising himself , went to the city early one morning , when , accosting the cobbler , he was told of the job he had , who for six pieces of gold , allowed himself to be blindfolded , and traced out the house of cassim , which the robber marked with chalk . buying nineteen mules and thirty-nine large jars , one full of oil , and the rest empty , the captain put a man into each jar , properly armed , and then proceeded to the street where alibaba dwelt . sir , said he , i have brought this oil a great way to sell , as i am quite a stranger , will you let me put my mules into your courtyard , and direct me where i may lodge to-night ? alibaba welcomed the pretended oil merchant , offered him a bed in his own house , and invited his guest in to supper . morgiana , sitting up later that night than usual , her lamp went out . she took her oil pot in her hand , and approaching the first jar , the robber within said is it time , captain ? she replied , no , not yet . so she ran back to the kitchen , and brought out a large kettle , which she filled with oil , set it on a great wood fire , and as soon as it boiled , she went and poured into the jars sufficient of the boiling oil to kill every man within . the captain of the robbers arose to assemble his men . coming to the first jar , he felt the steam of the boiled oil ! he ran hastily to the rest , and found every one of his troop put to death . full of rage , he forced the lock of the door , and made his escape over the walls . without letting any one into the secret , alibaba and morgiana the next night buried the thirty-nine thieves at the bottom of the garden . the captain at length , however , determined to adopt a new scheme for the destruction of alibaba . he removed all the valuable merchandise from the cave to the city , and took a shop exactly opposite to alibaba house . alibaba son went every day to his shop . the pretended cogia hassan soon appeared to be very fond of alibaba son , offered him many presents , and often detained him to dinner . alibaba thought it was necessary to make some return to these civilities , and he invited cogia hassan to supper , morgiana carried in the first dish herself . the moment she looked at cogia hassan , she knew it was the pretended oil merchant . she sent the other slaves into the kitchen , and waited at table herself , and while cogia hassan was drinking , she perceived he had a dagger hid under his coat . she went away , and dressed herself in the habit of a dancing-girl . as soon as she appeared at the parlor door , her master ordered her to come in to entertain his guest with some of her best dancing . morgiana danced several times before the assembled company , until , coming opposite cogia hassan , she drew a dagger from her girdle and plunged it into the robber heart . as a reward for her faithfulness , alibaba gave her in marriage to his son , and at his death put them in possession of his immense wealth ."
meaningless = [
    ".",
    ",",
    "!",
    "?",
    "the",
    "he",
    "and",
    "to",
    "a",
    "of",
    "was",
    "in",
    "had",
    "for",
    "it",
    "that",
    "but",
    "as",
    "with",
    "at",
    "i",
    "into",
    "be",
    "this",
    "me",
    "from",
    "then",
    "him",
    "his",
    "her",
    "she",
    "they",
    "them",
    "you",
]
word_list = alibaba.split()
vocab = {}

for w in word_list:
    if w in vocab:
        vocab[w] += 1
    else:
        vocab[w] = 1

for word in meaningless:
    del vocab[word]

vocab_final = sorted(vocab.items(), key=operator.itemgetter(1), reverse=True)

print(vocab_final, "\n")

# 빈도수 없이 단어만 출력
for k, v in vocab_final:
    print(k, end=" ")
print("\n")

# 단어만 알파벳순으로 정렬
print(sorted(vocab), "\n")  # 방법 1	// ['accosting', 'admission', 'adopt', ...]

for k, v in sorted(vocab.items(), key=operator.itemgetter(0)):
    print(k, end=" ")  # 방법2	// accosting admission adopt ...
