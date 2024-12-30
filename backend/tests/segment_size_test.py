from backend.src.text_processor import segment_text
from backend.src.emotion_analyzer import analyze_emotion
import json


def analyze_by_clauses(text):
    """
    Analyze text by segmenting it into clauses and detecting emotions for each clause.

    Args:
        text (str): The input text.

    Returns:
        list: A list of clauses with their detected emotions.
    """
    segmented = segment_text(text)
    results = []

    for paragraph in segmented:
        for sentence in paragraph["sentences"]:
            for clause in sentence["clauses"]:
                emotions = analyze_emotion(clause["text"])
                results.append({
                    "text": clause["text"],
                    "emotions": emotions
                })

    return results


def analyze_full_text(text):
    """
    Analyze the entire text as a single chunk.

    Args:
        text (str): The input text.

    Returns:
        dict: A dictionary of emotions for the full text.
    """
    return analyze_emotion(text)


if __name__ == "__main__":
    # Sample texts
    texts = {
        "Text 1": "She was happy, but she felt nervous.",
        "Text 2": "He smiled and said nothing.",
        "Text 3": "You liked my green shirt. You never told me so – you weren’t one to tell me you liked things about me (or that you liked me). But I know you liked it because at the end of the night – when everyone had gone home, and I’d had just one too many drinks, and you were being the gentleman you so desperately wanted to be by waiting patiently while I dumped the contents of abandoned bottles down the drain and filled a trash bag with enough plastic cups to turn myself into a disgusted environmentalist for just a moment – you got handsy.",
        "Text 4": """
You liked my green shirt. You never told me so – you weren’t one to tell me you liked things about me (or that you liked me). But I know you liked it because at the end of the night – when everyone had gone home, and I’d had just one too many drinks, and you were being the gentleman you so desperately wanted to be by waiting patiently while I dumped the contents of abandoned bottles down the drain and filled a trash bag with enough plastic cups to turn myself into a disgusted environmentalist for just a moment – you got handsy.
That was how you would phrase it. You had warned me early in the relationship that it was a habit of yours. You asked what my language of love was and had explained you couldn’t express affection without touch. “Even with the guys. You’ve seen it.” I had seen it. Your signature move of comedic relief was to silently place your hand in another guy’s hand during group conversations. You picked your targets wisely – always someone who was in on the joke, at the ready for a squeeze back, each of you pretending it was an intimate moment while knowing you’d gotten the attention of whoever else was in the car or around the kitchen island. You’d smile that little amused smile – bashful, no teeth.
You were self-conscious of your teeth. You mentioned once or twice you’d like to whiten them or that you hadn’t needed braces enough to get them, but the spacing and sizing were still off. But the real give away was when you bought the same toothpaste your best friend used. You said it was because you admired the shape of the tube – you probably did. You were hyper-conscious of aesthetics. It took you months to pick out a carpet the right shade of navy blue and pillowcases with the correct orange hue. You didn’t like the pillowcases you ordered. You took them off and left the naked white pillows to sit on your sofa.
Back to the toothpaste. If you’d copied it off anyone else, it might have been about the look of it alone. But it wasn’t anyone. It was him. His father was a dentist, and he had a whitening-strip addiction. You commented time and again how perfect his smile was. Once, when you were in a particularly self-loathing mood, you sat slumped in the corner of the booth of the dive bar we frequented, took out the permanent marker that made a home in your pocket, and silently drew napkin portraits of everyone at the table. You drew him and his bright smile. His “perfect little nose.” You drew your own silhouette like the goo in a lava lamp – forehead, nose, and chin jutting out like molten liquid seeping from the rest of your face.
The look of things – that’s what you loved. You wanted us to go out dressed in all black, so we’d match. You went through a phase where you wanted nothing more than to see me in a jumpsuit like the ones car mechanics wear. Monochrome. Monotone. You didn’t like eye colors that had multiple pigments in them. Brown was your favorite eye color – deep, dark irises. Simple things, you said.
The shirt I wore that night was green. Well, it was as close to green as I owned. I was throwing a Leap Day party, and I’d somehow gotten it into my head that I had to wear green. It was more of an olive grey. But it was a solid color, long-sleeved, and it had a scooped neckline that the Victorians would be proud of. I also wore the earrings you bought for me in San Diego. They weren’t my style. They were bronze, I wore silver. They dangled, I wore studs. But we had been fighting, and I knew you’d like to see them on me.
To be fair, I suppose the argument had been one sided. “I thought we got over this, my dear,” you said to me when I brought it up again while setting up for the party. You had gotten over it, I was quick to inform. I was still miffed that after three months of being in an exclusive relationship – after you had made it clear you wanted me nowhere near another man – that you refused to call yourself my boyfriend. You told me it was because you didn’t believe in that kind of relationship. You believed in courting, engagement, and marriage. We were courting. I was not your girlfriend.
The thing about labels is that they only make a difference to those who read them, and very few people were allowed to read our story. Of the two dozen mutual friends and acquaintances in our regularly scheduled lives, you were comfortable with six of them knowing we were romantically involved. And they were sworn to secrecy.
One of them was, of course, your best friend. He had to know because of the mess I’d made there. The summer before he met his fiancée, we’d spent almost every day together. He was in grad school, and I was working part-time after college graduation, so we had plenty of time to spare. We went to coffee shops, to bakeries, to liquor stores. One night your best man, who lived in the apartment complex across from mine, emerged at four o’clock in the morning to catch a flight, and found us “stooping it” on my front steps. He suspected feelings. I suspected he was right.
I sometimes wonder if it would have worked out between your best friend and myself, had I been more mature. But I was 22 and still thought I knew the kind of guy I wanted. So when I went to concerts with him, I hoped you’d have a ticket too; when we went for drinks, I hoped you’d come pull out a chair at our four-top. Once we were both working on our laptops at a café, and I had him give me a ride home so that I could wait for him to drive off and immediately walk out the door. You had sent me a text while I was with him, a casual ask if I was anywhere near the park at the summit and wanted to join you.
Eventually I told him I had feelings for you. That was when he admitted his feelings for me. He also told me he wanted us to be happy. My stomach tightened. I wasn’t even on your radar. I was toying with his emotions when you weren’t even an option. He had told me one night when the three of us were watching a movie at your apartment, when I had gone into the bathroom, you asked him where you should sit so that he and I could be together. Each of you, ready for the other to have me, if he wished. “We won’t be happy,” I mumbled.
And so your best friend knew about us now. You wouldn’t have moved forward without his blessing. Your best man knew too. That had been your committee. For months, you told me, you had debated it. Whether you wanted me. In the end, you decided you “didn’t want someone else to snatch me up” if you didn’t do it.
Apart from them, two of my closest confidantes, and a mature couple we knew in their late twenties, it was hush-hush. Co-workers and family were fine, but you didn’t want our immediate community meddling. The spotlight would have been too harsh for your liking in a group where everybody knew something, and Somebody knew everything. It was best, you said, to let it grow on its own before exposing it. I’m still not sure what it was.
You preferred things to stay on a need-to-know basis. Where you went every Monday night: this I could know (out of town to your aunt and uncle’s for dinner). What topics you discussed with your friends when I wasn’t there: this I rarely needed to know. Who you had dated – courted, I should say – before me: this I did not need to know.
The world did not need to know about us. When you were invited out by mutual friends, there was no automatic plus-one extended. When we went to dinner with a group, there was no seat saved for me. When my birthday drinks rolled around, the most I could expect was a knee pressed against mine as you talked to the person on your other side. Though we did almost give it away that night. We’d all been drinking, and it was the rarest of occasions when then whole group was willing to get up and dance. At one point, we clasped hands. We were off beat, and you almost fell. That was our last interaction of the night. BW – the only one in our party that night who knew about us – told me you’d stood with him at the bar. “You’re a good one, BW. Not like me.”
But you tried to be a good one. You would hardly kiss my cheek for the first couple of months. You weren’t sure if it was appropriate. Our first kiss, you wanted to be special. To mean something. I screwed that up for us with my impatience. You might remember, we weren’t the only couple to pair up that fall.
Three couples – four if you count JG and LH, but hardly anyone does. Your best friend and the girl he’d recently met at a wedding, our friend CG and your best friend’s new roommate, and us. While those couple had formed almost instantly after first glances, we had been around each other for about a year. You didn’t remember our first meeting – when we’d been the only two who showed to help a friend move out of his apartment. Your first memory fell half a year later, when I’d come with BW to your apartment. I remembered that too. We talked about work, and you explained what an industrial designer does by pointing out the buttons on your microwave. Your job was to figure out how to lay out things like that – microwaves, washing machines, headphones – so they looked nice to the user.
On the night of our first kiss, we were at a brewery for a friend’s birthday. We had taken a risk and walked there together, but we separated immediately upon arrival. You found out later only one keen set of eyes had noticed – your best man’s roommate, who had asked your best man about it – but she knew how to keep to herself. I talked to CG and your best friend’s roommate that night. They were planning a daytrip to NYC – something they did frequently. Their first date had been over twelve hours long, with half of it driving down and back. The extravagance of it was not out of character for the pair.
Your best friend was there with his girlfriend as well. She and I exchanged greetings, but the conversation quickly fizzled. She told your best friend later that she thought we were going to talk, but then we just…didn’t. I didn’t mean to be rude. The only things running through my head when I talked to her had to do with how much I missed my friend. Was I going to tell her that I’d pulled back from the fragments of my relationship with him when they’d started dating? That I hadn’t wanted to make her uncomfortable by continuing to spend hours a day with the guy she was seeing? I wasn’t a martyr by any stretch of the imagination, but I couldn’t be friends with her. I didn’t know how. If I couldn’t tell her the things burning up my mind – because her relationship fell in the center of them – what was there to talk about that was of any substance?
It was the middle of January, I was cold, I was tired, and I left. I walked home. I often walked home too late and too alone for a small girl in a city, so I called VR – one of my picks during the lineup for our game of covert relationship dodgeball. You texted me while I talked to her, and I saw them when I got home. You were peeved that I had left by myself, and you were going to the after-party at another Fenway bar.
We lived so close to each other that our buildings shared a back parking lot, and you stopped by to see me before going home that night. We sat on the couch, and you wondered why I had left the brewery. Why I hadn’t told you. I hadn’t seen you the whole night, so there wasn’t much of a goodbye needed. You insisted you could have driven me, but I needed the walk to think. You had had enough to drink at the bar that you didn’t press it. Your guard was down.
Somehow we ended up lying down, and I had you pinned. I stared at you, and your big blue eyes grew heavy with alcohol. I kept my face close to yours. I wasn’t going to cross that line – whether out of respect or fear of rejection remained unknown. You wanted this to mean something. I would make myself available, as I had always done. I would be there if you wanted it. Closer and closer. Watching. Waiting.
You closed the distance. At first it was only contact, not a kiss. Parted lips, hot breath, but not a kiss. Not romantic, not even sexual. More like a middle-school experiment. I brought the vinegar, you brought the baking soda. We lingered there, not yet willing to set off the reaction. After a few moments, we let the volcano erupt.
We had spoken about boundaries, but it was vague. It wasn’t I won’t touch you here, and you don’t touch me that way, but more along the lines of wanting to remain respectable. But respectability demands an audience. A person can’t be respectable if there’s no one to be respected by, and we were still on our own. Still, you were conscious of where you placed your hands, and you gave yourself no reason to feel shame.
Then I wore my green shirt. You had been careful all evening. You arrived early, but no one would think twice given the nearness of your apartment. When CG came into my room to check her makeup, you hid behind the door. The only moment you approached me after that was when I was alone in the kitchen – taking a breath – and after a glance toward the door and a peck, you disappeared back into the crowd.
Now we were alone, bodies buzzed from beer and sneaking around, like we’d stolen a bottle from a grown-up’s liquor cabinet. Instead of tracing curves of glass, your hands traced my frame.
"""
    }

    for title, full_text in texts.items():
        print(f"\n===== {title} =====")

        # Analyze by clauses
        print("\nAnalyzing by clauses:")
        clause_results = analyze_by_clauses(full_text)
        print(json.dumps(clause_results, indent=4))

        # Analyze as full text
        print("\nAnalyzing full text:")
        full_text_emotions = analyze_full_text(full_text)
        print(json.dumps(full_text_emotions, indent=4))