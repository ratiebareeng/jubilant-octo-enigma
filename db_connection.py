from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import certifi

uri = "mongodb+srv://ratie:c9ydQe0B0YYiGNo4@jibulant-octo-enigma.qzu5j.mongodb.net/?retryWrites=true&w=majority&appName=jibulant-octo-enigma"

# MongoDB connection setup
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'), tlsCAFile=certifi.where())
#client = MongoClient(uri, server_api=ServerApi('1'))

#Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged Jubilant Octo Enigma deployment. Successfully connected to MongoDB!")
except Exception as e:
    print(f"Failed to connect to DB: \n{e}")

db = client['dev_lyrics_db']  # Database name
songs_collection = db['songs']  # This will be the collection where we store the songs


def save_song_to_mongodb(song):
    # Check if the song already exists in the database
    existing_song = songs_collection.find_one({'url': song['url']})

    if existing_song:
        print(f"{song['title']} already exists in the database")
    else:
        # Insert the song into the database
        result = songs_collection.insert_one(song)
        print(f"Saved {song['title']} to MongoDB with id: {result.inserted_id}")


def save_songs_to_mongodb(songs):
    for m_song in songs:
        try:
            save_song_to_mongodb(m_song)
        except Exception as e:
            print(f"Error saving {m_song['title']}: {str(e)}")


# song = [
#     {
#         "artist": "Nipsey Hussle",
#         "lyrics": "[Intro: Stacy Barthe & Arctic Monkeys]\nWoah-oh\nWoah-oh\nWoah-oh\nLike the beginning of Mean Streets, you could (Oh)\nLike the beginning of Mean Streets, you could\nLike the beginning of Mean Streets, you could\n\n[Verse 1: Nipsey Hussle & Arctic Monkeys]\nI'm prolific, so gifted\nI'm the type that's gon' go get it, no kiddin'\nBreaking down a Swisher front of your buildin'\nSitting on the steps, feeling no feelings\nLast night, it was a cold killin'\nYou gotta keep the devil in his hole, nigga\nBut you know how it go, nigga\nI'm front line every time it's on, nigga\nHunnid proof flow, run and shoot pro\n458 drop, playin' \"Bullet Proof Soul\"\nEvery few shows, I just buy some new gold\nCircle got smaller, everybody can't go\nDowntown, Diamond District, jewelers like, \"Yo\nHussle, holla at me, I got Cubans on the low\"\nFlew to Cancun, smokin' Cubans on the boat\nThen docked at Tulum just to smoke, look\nListening to music at the Mayan Ruins\nTrue devotion on the bluest ocean, cruisin'\nMy cultural influence even rival Lucien\nI'm integrated vertically, y'all niggas blew it\nThey tell me, \"Hussle, dumb it down, you might confuse 'em\"\nThis ain't that weirdo rap you motherfuckers used to\nLike the beginning of Mean Streets\nI'm an urban legend, South Central in a certain section\nCan't express how I curved detectives\nGuess it's evidence of a divine presence, blessings\nHeld me down, at times, I seem reckless, F it\nYou got an L, but got an E for effort, stretched him\nDropped him off in the Mojave desert, then left him\nAin't no answer to these trick questions\nMoney Makin' Nip, straighten out my jewelry on my bitch dresser\nWell known, flick up and jail pose\nSnatch a champagne bottle from Rico's 'til T show\nWhatever, nigga, playin' chess, not checkers, nigga\nThirty-eight special for you clever niggas\nSee, bro, if you ain't live and die by the street code\nBeen through all these motions, up and down like a see-saw\nI can never view you as my equal\nFuck I wanna hear your CD for?\n",
#         "title": "Victory Lap by Nipsey Hussle (Ft. Stacy Barthe)",
#         "url": "https://genius.com/Nipsey-hussle-victory-lap-lyrics"
#     },
#     {
#         "artist": "Nipsey Hussle",
#         "lyrics": "[Chorus: Nipsey Hussle & Belly]\nDouble up\nThree or four times, I ain't tellin' no lies, I just run it up\nNever let a hard time humble us\nDouble up\nI ain't tellin' no lies, I just (Yeah)\nI ain't tellin' no lies, I just\nFive, four, three, two\nThat's time I got to you\nThat money, my dreams come true\nMy life in diamonds, who knew?\nWho knew?\nWho knew?\n\n[Verse 1: Nipsey Hussle]\nTurned seven to a fourteen\nFourteen to a whole thing\nLord knows it's a cold game\nSwitched up on you hoes, man\nBig body take both lanes\nBackseat, blowin' propane\nAll-black, five gold chains\nYoung rich nigga bossed up on his own, man\nMy new shit sound like it's \"Soul Train\"\nTookie Williams over Coltrane\nEric B by the rope chain\nRSC, we for sure bang\nTiny Locs and they go crazy\nWhat you know about the dope game?\nWas you born in the '80s? Did your mama smoke cocaine?\nHave you ever seen a whole thang?\nBut you drove to the streets 'cause you grew up on short change?\nFucked up when the dope age\nIt remind me when these rappers drop duds and they quotes change\nHad the part with the low fade\nI would stand in front of Nix with my sack for the whole day\nDrive-bys, that was road rage\nThen we park and hop out, learn levels to this whole thang\nOld school, play the O'Jays\nTryna make a slow change, mama still slavin' for a low wage\nTryna\n",
#         "title": "Double Up by Nipsey Hussle (Ft. Belly & DOM KENNEDY)",
#         "url": "https://genius.com/Nipsey-hussle-double-up-lyrics"
#     },
#     {
#         "artist": "Nipsey Hussle",
#         "lyrics": "[Intro: Roddy Ricch]\n(Hit-Boy)\nYeah, yeah, yeah, yeah\n(TrapAdix)\nYeah, yeah, yeah, yeah\nYeah, I was ridin' ’round in the V-12 with the racks in the middle\nI was ridin' 'round in the V-12 with the racks in the middle\nYeah, yeah, yeah, yeah\nAy\n\n[Chorus: Roddy Ricch]\nI was riding ’round in the V-12 with the racks in the middle\nHad to pray to almighty God they let my dog out the kennel\nWhen you get it straight up out the mud, you can't imagine this shit\nI been pullin' up in the drop tops with the baddest bitches\nYoung nigga been focused on my check (Mhmmhm)\nGot a new coupe wrapped around my neck (Mhmmhm)\nTryna put the water on my Patek (Mhmmhm)\nI got killers to the left of me (Mhmmhm)\n\n[Verse 1: Nipsey Hussle]\nWe was lurking on 'em, ain't show no mercy on 'em\nWe was goin' back to back, we put a curfew on 'em\nIt was dark clouds on us, but that was perfect for us\nWe know you always crash and burn, but it was working for us\nLimo tint the V-12, double check the details\nGotta cross my T’s and dot my I’s or I can't sleep well\nMillions off of retail\nOnce again, I prevail\nKnew that shit was over from the day I dropped my presale\nHold up, let the beat build\nSee me in the streets still\nI been fightin’ battles up a steep hill\nThey gave my road dog twelve, it was a sweet deal\nAnd I been ridin' solo tryna rebuild\nLook\n",
#         "title": "Racks in the Middle by Nipsey Hussle (Ft. Hit-Boy & Roddy Ricch)",
#         "url": "https://genius.com/Nipsey-hussle-racks-in-the-middle-lyrics"
#     },
#     {
#         "artist": "Nipsey Hussle",
#         "lyrics": "[Verse 1: Nipsey Hussle]\nLook, my nigga this is dedication, this is anti-hesitation\nThis a real nigga celebration\nThis a Dime Blocc declaration\n59th and 5th Ave, granny house with vanilla wafers\nThis the remedy, the separation\n2Pac of my generation, blue pill in the fuckin' Matrix\nRed rose in the gray pavement\nYoung black nigga trapped and he can't change it\nKnow he a genius, he just can't claim it\n'Cause they left him no platforms to explain it\nHe frustrated so he get faded\nBut deep down inside he know you can't fade him\nHow long should I stay dedicated?\nHow long 'til opportunity meet preparation?\nI need some real nigga reparations\n'Fore I run up in your bank just for recreation\n\n[Chorus: Nipsey Hussle]\nDedication, hard work plus patience\nThe sum of all my sacrifice, I'm done waitin'\nI'm done waitin', told you that I wasn't playin'\nNow you hear what I been sayin'\nDedication\nIt's dedication, look\n",
#         "title": "Dedication by Nipsey Hussle (Ft. Kendrick Lamar)",
#         "url": "https://genius.com/Nipsey-hussle-dedication-lyrics"
#     },
#     {
#         "artist": "Nipsey Hussle",
#         "lyrics": "[Verse 1: Nipsey Hussle]\nPull up in motorcades, I got a show today\nThis all I'm tryna do, hustle and motivate\nChoppers a throwaway, hustle the Hova way\nThat's why they follow me, huh? They think I know the way\n'Cause I took control of things, ballin' the solo way\nAnd if you pattern my trend, I make you my protege\nSlauson Ave soldier raised, niggas don't know them days\nTake you in back of the buildings, make you expose your age\nTake you across the tracks, make you explode a face\nNow you official now, but you got a soul to save\nI just been cookin' that new, I'm 'bout to drop in a few\nThink if I call it the great, the people gon' call it the truth\nAin't really trip on the credit, I just paid all of my dues\nI just respected the game, now my name all in the news\nTrippin' on all of my moves, quote me on this, got a lot more to prove\nRemember I came in this bitch fresh out the county with nothin' to lose\n\n[Chorus: Maurice David Wade]\nAnd I don't do this for nothin', nah, from the ground up, yeah\nBut I don't do this shit for nothin', no, no, not at all, yeah\nMy mama need rent, ma need rent, yeah, she do, aw yeah\nSo I don't do this shit for nothin', no, not at all, all\nI told her I got it, oh, yeah\nSo I don't do this shit for nothin', not at all, from the ground up\nHustle and motivate (Woo)\n",
#         "title": "Hussle & Motivate by Nipsey Hussle",
#         "url": "https://genius.com/Nipsey-hussle-hussle-and-motivate-lyrics"
#     },
#     {
#         "artist": "Nipsey Hussle",
#         "lyrics": "[Chorus]\nOh, aw, baby, it's been so long\nOh, aw, baby, it's been so long\n\n[Verse 1]\nMogul and they know that, logo on my floor mat\nCourtside, Chamberlain throwback match my Rolex\nEverywhere I go, flex, valet park on some Loc shit\nWhole lot of smoke in that 'Rari, that thang potent\nBurnin' rubber, wearin' cameras, they was undercovers\nUnder pressure, made statements, turned on they brothers\nNever judge you, but the streets'll never love you\nI wonder what it come to in your brain for you to run to\nOnes that hate us, handcuff us and mace us\nCall us dumb niggas 'cause our culture is contagious\nThird-generation South Central gangbangers\nThat lived long enough to see it changin'\nThink it's time we make arrangements\nFinally wiggle out they mazes\nFind me out in different places\nI'm the spook by the door, this the infiltration\nDouble back dressed in blue laces\n\n[Chorus]\nOh, aw, baby, it's been so long\nOh, aw, baby, it's been so long\n",
#         "title": "Blue Laces 2 by Nipsey Hussle",
#         "url": "https://genius.com/Nipsey-hussle-blue-laces-2-lyrics"
#     },
#     {
#         "artist": "Nipsey Hussle",
#         "lyrics": "[Chorus]\nAll my life, been grindin' all my life\nSacrificed, hustled, paid the price\nWant a slice, got to roll the dice\nThat's why all my life, I been grindin' all my life, look\nAll my life, been grindin' all my life (Yup)\nSacrificed, hustled, paid the price (Woah)\nWant a slice, got to roll the dice\nThat's why all my life, I been grindin' all my life, look\n\n[Verse 1]\nI'm married to this game, that's who I made my wife\nSaid I'd die alone, I told that bitch she probably right\nOne thing that's for sure, not a stranger to this life\nGot a safe that's full of Franklins and a shoulder full of stripes (Ah)\nDon't know a nigga like myself\nI say self-made meanin' I designed myself\nCounty jail fades, you could pull my file yourself\nSpot raid, swallow rocks, I'm gettin' high myself\nLook, and damn right, I like the life I built\nI'm from Westside, 60, shit, I might got killed\nStandin' so tall, they think I might got stilts\nLegendary baller like Mike, like Wilt\n'96 Impala, thug life on wheels\nUp against the walls, squabble at Fox Hills\nLike a motherfuckin' boss, ask me how I feel\nSuccessful street nigga touchin' them first mils (Woah)\n",
#         "title": "Grinding All My Life by Nipsey Hussle",
#         "url": "https://genius.com/Nipsey-hussle-grinding-all-my-life-lyrics"
#     },
#     {
#         "artist": "Nipsey Hussle",
#         "lyrics": "[Chorus: Nipsey Hussle]\nLast time that I checked\nIt was five chains on my neck\nIt was no smut on my rep\nLast time that I checked (Checked)\nI was sellin' zones in the set (Zones up in the set)\nMake a quarter mil' no sweat\nLast time that I checked\nI'm the streets' voice out West\nLegendary, self-made progress\nLast time that I checked (Checked)\nFirst, you get the money, then respect\nThen the power and the hoes come next\nLast time that I checked (Checked)\n\n[Verse 1: Nipsey Hussle]\nI been self-made from the dribble\nI was been sayin' I'ma kill em, look\nPlaying no games with you niggas\nPop clutch, switch lanes on you niggas, look\nI laid down the game for you niggas\nTaught you how to charge more than what they paid for you niggas\nOwn the whole thing for you niggas\nReinvest, double up, then explain for you niggas\nIt gotta be love, who run the city? It gotta be cuz\nThis for the pieces I took off the Monopoly board\nAnd y'all niggas' false claims, it gotta be fraud\nJust keep the hood up out your mouth or you gotta be charged\nI doubled up, tripled up, nigga, what?\nBanged on the whole game, I ain't give a fuck\nNobody trippin', handled business, got my digits up\nAnd when I drop, you know I'm 'bout to fuck the city up\n",
#         "title": "Last Time That I Checc'd by Nipsey Hussle (Ft. YG)",
#         "url": "https://genius.com/Nipsey-hussle-last-time-that-i-checcd-lyrics"
#     },
#     {
#         "artist": "Nipsey Hussle",
#         "lyrics": "[Produced by 9th Wonder]\n\n[Intro: Sample]\nWhen all dreams seem to die\nThe summer's gone, the breeze stops blowing\nThe sun just leaves the sky\n\n[Verse 1]\nYeah\nUh\nYeah, this your life, you can play with it\nYou make your bed, you gon' lay in it\nDo your thing, just be safe with it\nTriple bunks in the state prison\nBlue laces in my blue chucks\nI ain't never gave two fucks\nBET I chucked the hood up\nAsking if that nigga Nip hood, what\nLike I wouldn't take it to the back with you\nSame nigga walk the track with you\nSame nigga shot a strap with you\nSame nigga bought a sack with you\nNineteen touchin' two birds\nAlpinas off a few swerves\nGrey leather in my white Lincoln\nShit smellin' like a new purse\nTwo C's on my bitch shit\nMy money risin' like Bisquick\nSix words help you get this\nRich Rapper On Some Crip Shit\nI prayed for blessings as a young nigga\nNot to learn the hard lessons of a drug dealer\nTriple life with a gang enhancement\nThe judge triple white and he hate your blackness\nSlam the gavel with a racist passion\nGot you waitin' on appeals but your patience passin'\nAll you've got to offer is a fight\nIt's too late to run to Christ once you caught up in this life\nLook\n",
#         "title": "Face the World by Nipsey Hussle",
#         "url": "https://genius.com/Nipsey-hussle-face-the-world-lyrics"
#     },
#     {
#         "artist": "Nipsey Hussle",
#         "lyrics": "[Intro]\nIt's that 4 in the morning shit\n\n[Verse]\nI'm off this Red Bull\nI got a head full\nA nigga stressed out, let's get this bed full\nSexual healing; so appealing\nYou a bad bitch, I'm a real nigga\nTell me that you love me\nI tell you the same\nThat's a fucking shame\nWe both runnin' game\nI just want your pleasure\nYou just want my pain\nI just want you all for me and you just want the same\nLet's take a flight; let's live this life\nLet's get a hotel, let's both spend a night\nI'm a busy nigga, you a busy girl\nIt's a fast life we liven' in this busy world\nWe in my fast car, you ain't no fast broad\nYou got yo' heart broke, he did yo' ass wrong\nPlus yo' dad gone, let me be yo' daddy\nI wanna see you happy we both come from broken families\nYou can tell the truth, I'mma tell it too\nWe gon' smoke this weed 'til they kick us out the room\nLike fuck it, that's life\nFuckin' tonight; we fuckin' right?\nYou fuckin' right\nI ain't goon' lie to you; I know I'm fly to you\nNah, fuck that girl I'm the sky to you\nOcean in the clouds; birds and the bees\nYour friends proud when they know that you fuckin' with me\nI got you poppin', I'll take you shoppin'\nAround the world; started on Slauson\nThat's real shit; real shit\nI know all my real bitches feel this\n4 in the morning, tell me that you want it\nBend you over, I got you moaning\nYou love this shit, you want this shit\nYou got this shit, no politics\n",
#         "title": "4 in the Mornin by Nipsey Hussle",
#         "url": "https://genius.com/Nipsey-hussle-4-in-the-mornin-lyrics"
#     },
#     {
#         "artist": "Nipsey Hussle",
#         "lyrics": "[Chorus: Nipsey Hussle]\nAnd this is what it feels like (Feels like, feels like)\nAnd this is what it feels like (Feels like, feels like)\n\n[Verse 1: Nipsey Hussle]\nLook, the only reason I survive 'cause a nigga is special, first\nYou get successful, then it get stressful, thirst\nNiggas gon' test you, see what your texture's worth\nDiamonds and pipes, one of 'em pressure bursts\nStreet nigga, still I get checks, in spurts\nI'm for peace, but before I get pressed, I murk\nBetter days pray for but expectin' worse\nAt this level, bullshit, I'm just less concernеd\nCruisin' in the 6, lookin' at the proceeds of rap music on my wrist\nDrop another mixtapе, my shit boomin' out this bitch\nYoung Malcolm, I'm the leader of the movement out this bitch, look\nAnd this is what it feels like (Feels like)\nReach a level, make you question, \"Is it real life?\"\nAll the weed good, all the pussy real tight\nAnd the only rule, keep your dollar bills right\n\n[Chorus: Nipsey Hussle]\nAnd this is what it feels like (Feels like, feels like)\nAnd this is what it feels like (Feels like, feels like)\nAnd this is what it feels like (Feels like, feels like)\nAnd this is what it feels like (Feels like, feels like)\n",
#         "title": "What It Feels Like by Nipsey Hussle & JAY-Z",
#         "url": "https://genius.com/Nipsey-hussle-and-jay-z-what-it-feels-like-lyrics"
#     },
#     {
#         "artist": "Nipsey Hussle",
#         "lyrics": "[Intro: PARTYNEXTDOOR & Nipsey Hussle]\nStrippers in the club and my cup's half empty\nRide with my niggas 'cause my niggas understand me\nStill on Plan A, pussy niggas on Plan B\nRight now (Young rich nigga, young rich nigga)\nMotherfucker, let's go\n\n[Verse: Nipsey Hussle & Puff Daddy]\nYeah, what could make a nigga wanna go and get it?\nSaid he want a Bimmer with the subs in it\nSaid he grew up in the house and it was love missin'\nSaid he grew up in the set, he keep his gun with him\nYoung nigga, young nigga (Let's go)\nYoung (Niggas), just a young nigga\nAnd he don't need a reason, he a young nigga (That's right)\nAnd you don't want your daughter and your sons with him\nYoung nigga, just a young nigga (Let's go)\nYoung nigga, just a young nigga\nProbably never understand us (Don't stop)\n'Til he pull up in a Phantom (Don't stop)\nWhen he pull up in a Phantom\nHe gon' have that shit blastin' (That's right)\nLike young nigga, just a young nigga\nYoung nigga, just a young nigga\nWhat they call you where you from, nigga? (Where you from, nigga?)\nIn my city, that was question number one, nigga (Number one, nigga)\nLookin' at the legend I become, nigga (Look at him)\nI can't help but feeling like I am the one, nigga (Your turn)\nRemember I was on the run, nigga (Let's go)\nCouple years before you had a son, nigga (Let's go)\nOpen up your doors and kept it one with me\nHeld a nigga down and that was love, nigga (Let's go)\nNobody wanna stand in front a judge, nigga (Yeah)\nMake you think of better days like when you was winnin'\nStandin' on the couches in the club with us\n(We all in here, you see it motherfucker, young nigga)\nThen I got my shot, I had to run with it\nOut the gate, lost count\nMany days in the studio we slaved, but this shit we gotta say\nStaring into space as you fishing for a phrase\nUninspired, in your mind, still, it's all a paper chase\nFirst you overdedicate, then you notice that you great\nAnd you been the whole time, and it slap you in your face\nThen you stack it in your safe, got it crackin', it was fate\nNow you the definition, nigga, laughin' to the bank\nI'm a master of my fate\nPlus I'm the type of nigga own the masters to my tapes\nIn Nevada for the day\nI caught a flight from Philly, we just sold out TLA\nFresh up off of stage on my way to B of A\nAMB, we LA, tryna eat, we the way\nLook, young Nipsey the great\nNever taught how to drink, I just lead to the lake\nIt's eighty-something degrees in LA (Yeah)\nFuck it, time to put some jet-skis on the lake\nLook, I got a team in my bank\nI don't even need an ID at my bank\nThis used to be a dream we would chase\nI know J. Stone and Cobby Supreme could relate\nI know the whole team could relate\nI know Evan McKenzie and Bron Lees could relate\nCornell, Saddam, Adam Andebrhan\nSteven Donelson and Blacc Sam been on this marathon\nBallin' since my brother used to hustle out the Vons\nCouple hundred thousand up, he took a shovel to the lawn\nNo exaggeration for the content of my songs\nWhen he went to dig it up, shit, a hundred somethin' gone\nMolded, you can ask moms\nHad to plug in blow dryers for the ones that we could wash (Let's go)\nSalvaged a little bit, young rich nigga shit\nPressure on your shoulder, how you gon' deal with it? (Come on)\nSay it's uncomfortable (That's right), when you transitionin' (Let's go)\nBut it's so beautiful (Don't stop), when you get rich in it (Don't stop)\nWhen you start killin' shit (Elevate) and they all witness it (Keep risin')\nMoney grow faster (Keep goin'), than niggas can spend the shit (Keep showin')\nOpen more businesses (Get down), with you and your niggas, they (Let's go)\nWatchin' your vision (Don't stop), and being more generous (Get money)\nFuck a Ford dealership (Yeah, c'mon), we up in Forbes (Number one, motherfuckers, every year)\nWatching and they wishin' that it wasn't yours (Let's go)\nI forgive you, I remember I was poor (Not no more)\nPlus I ain't in the way of what you reachin' for (Yeah)\nYou gotta play the game, you gotta read the score (Read the score)\nSee, I'ma do the same and pop the clutch of foreign (Let's go)\nTold me if I want it, gotta hustle for it (Get it, get it)\nOnly difference now, the money more mature\n",
#         "title": "Young Nigga by Nipsey Hussle (Ft. Diddy)",
#         "url": "https://genius.com/Nipsey-hussle-young-nigga-lyrics"
#     }
# ];
# save_songs_to_mongodb(song)

