import random

def getJudgment(hexagram):
	if hexagram == 1:
		return """
		Ch\'ien: The Creative.\n
		The creative works through sublime success,
		Furthering through perseverance.
		"""
	elif hexagram == 2:
		return """
		K\'un: The Receptive.\n
		The receptive brings about sublime success,
		Furthering through the perseverance of a mare.
		If the superior man undertakes something and tries to lead,
		He goes astray;
		But if he follows, he finds guidance.
		It is favorable to find friends in the west and south,
		To forego friends in the east and north.
		Quiet perseverance brings good fortune.
		"""
	elif hexagram == 3:
		return """
		Chun: Difficulty at the Beginning.\n
		Difficulty at the Beginning works supreme success,
		Furthering through perseverance.
		Nothing should be undertaken.
		It furthers one to appoint helpers.
		"""
	elif hexagram == 4:
		return """
		Meng: Youthful Folly.\n
		Youthful Folly has success.
		It is not I who seek the young fool;
		The young fool seeks me.
		At the first oracle I inform him.
		If he asks two or three times, it is importunity.
		If he importunes, I give him no information.
		Perseverance furthers.
		"""
	elif hexagram == 5:
		return """
		Hsu: Waiting (Nourishment.)\n
		Waiting. If you are sincere,
		You have light and success.
		Perseverance brings good fortune.
		It furthers one to cross the great water.
		"""
	elif hexagram == 6:
		return """
		Sung: Conflict.\n
		Conflict. You are sincere
		And are being obstructed.
		A cautious halt halfway brings good fortune.
		Going through to the end brings misfortune.
		It furthers one to see the great man.
		It does not further one to cross the great water.
		"""
	elif hexagram == 7:
		return """
		Shih: The Army.\n
		The Army. The army needs perseverance
		And a strong man.
		Good fortune without blame.
		"""
	elif hexagram == 8:
		return """
		Pi: Holding Together (Union.)\n
		Holding Together brings good fortune.
		Inquire of the oracle once again
		Whether you possess sublimity, constancy, and perseverance;
		Then there is no blame.
		Those who are uncertain gradually join.
		Whoever comes too late
		Meets with misfortune.
		"""
	elif hexagram == 9:
		return """
		Hsiao Ch\'u: The Taming Power of the Small.\n
		The Taming Power of the Small
		Has success.
		Dense clouds, no rain from our western region.
		"""
	elif hexagram == 10:
		return """
		Lu: Treading (Conduct.)\n
		Treading. Treading upon the tail of the tiger.
		It does not bite the man. Success.
		"""
	elif hexagram == 11:
		return """
		T\'ai: Peace.\n
		Peace. The small departs,
		The great approaches.
		Good fortune. Success.
		"""
	elif hexagram == 12:
		return """
		P\'i: Standstill (Stagnation.)\n
		Standstill. Evil people do not further
		The perseverance of the superior man.
		The great departs; the small approaches.
		"""
	elif hexagram == 13:
		return """
		T\'ung J\u00EAn: Fellowship with Men.\n
		Fellowship with Men in the open.
		Success.
		It furthers one to cross the great water.
		The perseverance of the superior man furthers.
		"""
	elif hexagram == 14:
		return """
		Ta Yu: Possession in Great Measure.\n
		Possession in Great Measure.
		Supreme Success.
		"""
	elif hexagram == 15:
		return """
		Ch\'ien: Modesty.\n
		Modesty creates success.
		The superior man carries things through.
		"""
	elif hexagram == 16:
		return """
		Yu: Enthusiasm.\n
		Enthusiasm. It furthers one to install helpers
		And to set armies marching.
		"""
	elif hexagram == 17:
		return """
		Sui: Following.\n
		Following has supreme success.
		Perseverance furthers. No blame.
		"""
	elif hexagram == 18:
		return """
		Ku: Work on What Has Been Spoiled (Decay.)\n
		Work on What Has Been Spoiled
		Has supreme success.
		It furthers one to cross the great water.
		Before the starting point, three days.
		After the starting point, three days.
		"""
	elif hexagram == 19:
		return """
		Lin: Approach.\n
		Approach has supreme success.
		Perseverance furthers.
		When the eighth month comes,
		There will be misfortune.
		"""
	elif hexagram == 20:
		return """
		Kuan: Contemplation (View.)_\n
		Contemplation. The ablution has been made,
		But not yet the offering.
		Full of trust they look up to him.
		"""
	elif hexagram == 21:
		return """
		Shih Ho: Biting Through.\n
		Biting Through has success.
		It is favorable to let justice be administered.
		"""
	elif hexagram == 22:
		return """
		Pi: Grace.\n
		Grace has success. 
		In small matters
		It is favorable to undertake something.
		"""
	elif hexagram == 23:
		return """
		Po: Splitting Apart.\n
		Splitting apart. It does not further one
		To go anywhere.
		"""
	elif hexagram == 24:
		return """
		Fu: Return (The Turning Point.)\n
		Return. Success.
		Going out and coming in without error.
		Friends come without blame.
		To and fro goes the way.
		On the seventh day comes return.
		It furthers one to have somewhere to go.
		"""
	elif hexagram == 25:
		return """
		Wu Wang: Innocence (The Unexpected.)\n
		Innocence. Supreme success.
		If someone is not as he should be,
		He has misfortune,
		And it does not further him
		To undertake anything.
		"""
	elif hexagram == 26:
		return """
		Ta Ch\'u: The Taming Power of the Great.\n
		The Taming Power of the Great.
		Perseverance furthers.
		Not eating at home brings good fortune.
		It furthers one to cross the great water.
		"""
	elif hexagram == 27:
		return """
		I: The Corners of the Mouth (Providing Nourishment.)\n
		The Corners of the Mouth.
		Perseverance brings good fortune.
		Pay heed to the providing of nourishment
		And to what a man seeks
		To fill his own mouth with.
		"""
	elif hexagram == 28:
		return """
		Ta Kuo: Preponderance of the Great.\n
		Preponderance of the Great.
		The ridgepole sags to the breaking point.
		It furthers one to have somewhere to go.
		Success.
		"""
	elif hexagram == 29:
		return """
		K\'an: The Abysmal (Water.)\n
		The Abysmal repeated.
		If you are sincere, you have success in your heart,
		And whatever you do succeeds.
		"""
	elif hexagram == 30:
		return """
		Li: The Clinging, Fire.\n
		The Clinging. Perseverance furthers.
		It brings success.
		Care of the cow brings good fortune.
		"""
	elif hexagram == 31:
		return """
		Hsien: Influence (Wooing.)\n
		Influence. Success.
		Perseverance furthers.
		To take a maiden to wife brings good fortune.
		"""
	elif hexagram == 32:
		return """
		H\u00EAng: Duration.\n
		Duration. Success. No blame.
		Perseverance furthers.
		It furthers one to have somewhere to go.
		"""
	elif hexagram == 33:
		return """
		Tun: Retreat.\n
		Retreat. Success.
		In what is small, perseverance furthers.
		"""
	elif hexagram == 34:
		return """
		Ta Chuang: The Power of the Great.\n
		The Power of the Great. Perseverance furthers.
		"""
	elif hexagram == 35:
		return """
		Chin: Progress.\n
		Progress. The powerful prince
		Is honored with horses in large numbers.
		In a single day he is granted audience three times.
		"""
	elif hexagram == 36:
		return """
		Ming I: Darkening of the Light.\n
		Darkening of the Light. In adversity
		It furthers one to be persevering.
		"""
	elif hexagram == 37:
		return """
		Chia J\u00EAn: The Family (The Clan.)\n
		The family. The perseverance of the woman furthers.
		"""
	elif hexagram == 38:
		return """
		K\'uei: Opposition.\n
		Opposition. In small matters, good fortune.
		"""
	elif hexagram == 39:
		return """
		Chien: Obstruction.\n
		Obstruction. The northwest furthers.
		The northeast does not further.
		It furthers one to see the great man.
		Perseverance brings good fortune.
		"""
	elif hexagram == 40:
		return """
		Hsieh: Deliverance.\n
		Deliverance. The southwest furthers.
		If there is no longer anything where one has to go,
		Return brings good fortune.
		If there is still something where one has to go,
		Hastening brings good fortune.
		"""
	elif hexagram == 41:
		return """
		Sun: Decrease.\n
		Decrease combined with sincerity
		Brings about supreme good fortune
		Without blame.
		One may be persevering in this.
		It furthers one to undertake something.
		How is this to be carried out?
		One may use two small bowls for the sacrifice.
		"""
	elif hexagram == 42:
		return """
		I: Increase.\n
		Increase. It furthers one
		To undertake something.
		It furthers one to cross the great water.
		"""
	elif hexagram == 43:
		return """
		Kuai: Break-through (Resoluteness.)\n
		Break-through. One must resolutely make the matter known
		At the court of the king.
		It is necessary to notify one's own city.
		It does not further to resort to arms.
		It furthers one to undertake something.
		"""
	elif hexagram == 44:
		return """
		Kou: Coming to Meet.\n
		Coming to Meet. The maiden is powerful.
		One should not marry such a maiden.
		"""
	elif hexagram == 45:
		return """
		Ts\'ui: Gathering Together (Massing.)\n
		Gathering Together. Success.
		The king approaches his temple.
		It furthers one to see the great man.
		This brings success. Perseverance furthers.
		To bring great offerings creates great fortune.
		It furthers one to undertake something.
		"""
	elif hexagram == 46:
		return """
		Sh\u00EAng: Pushing Upward.\n
		Pushing upward has supreme success.
		One must see the great man.
		Fear not.
		Departure toward the south
		Brings good fortune.
		"""
	elif hexagram == 47:
		return """
		K\'un: Oppression (Exhaustion.)\n
		Oppression. Success. Perseverance.
		The great man brings about good fortune.
		No blame.
		When one has something to say,
		It is not believed.
		"""
	elif hexagram == 48:
		return """
		Ching: The Well.\n
		The Well. The town may be changed,
		But the well cannot be changed.
		It neither decreases nor increases.
		They come and go and draw from the well.
		If one gets down almost to the water
		And the rope does not go all the way,
		Or the jug breaks, it brings misfortune.
		"""
	elif hexagram == 49:
		return """
		Ko: Revolution (Mounting.)\n
		Revolution. On your own day
		You are believed.
		Supreme success,
		Furthering through perseverance.
		Remorse disappears.
		"""
	elif hexagram == 50:
		return """
		Ting: The Caldron.\n
		The Caldron. Supreme good fortune.
		Success.
		"""
	elif hexagram == 51:
		return """
		Ch\u00EAn: The Arousing (Shock, Thunder.)\n
		Shock brings success.
		Shock comes--oh, oh!
		Laughing words--ha, ha!
		The shock terrifies for a hundred miles,
		And he does not let fall the sacrificial spoon and chalice.
		"""
	elif hexagram == 52:
		return """
		K\u00EAn: Keeping Still, Mountain.\n
		Keeping Still. Keeping his back still
		So that he no longer feels his body.
		He goes into his courtyard
		And does not see his people.
		No blame.
		"""
	elif hexagram == 53:
		return """
		Chien: Gradual Progress.\n
		Development. The maiden
		Is given in marriage.
		Good fortune.
		Perseverance furthers.
		"""
	elif hexagram == 54:
		return """
		Kuei Mei: The Marrying Maiden.\n
		The Marrying Maiden.
		Undertakings bring misfortune.
		Nothing that would further.
		"""
	elif hexagram == 55:
		return """
		F\u00EAng: Abundance (Fullness.)\n
		Abundance has success.
		The king attains abundance.
		Be not sad.
		Be like the sun at midday.
		"""
	elif hexagram == 56:
		return """
		Lu: The Wanderer.\n
		The Wanderer. Success through smallness.
		Perseverance brings good fortune
		To the wanderer.
		"""
	elif hexagram == 57:
		return """
		Sun: The Gentle (The Penetrating, Wind.)\n
		The Gentle. Success through what is small.
		It furthers one to have somewhere to go.
		It furthers one to see the great man.
		"""
	elif hexagram == 58:
		return """
		Tui: The Joyous, Lake.\n
		The Joyous. Success.
		Perseverance is favorable.
		"""
	elif hexagram == 59:
		return """
		Huan: Dispersion (Dissolution.)\n
		Dispersion. Success.
		The king approaches his temple.
		It furthers one to cross the great water.
		Perseverance furthers.
		"""
	elif hexagram == 60:
		return """
		Chieh: Limitation.\n
		Limitation. Success.
		Galling limitation must not be persevered in.
		"""
	elif hexagram == 61:
		return """
		Chung Fu: Inner Truth.\n
		Inner Truth. Pigs and fishes.
		Good fortune.
		It furthers one to cross the great water.
		Perseverance furthers.
		"""
	elif hexagram == 62:
		return """
		Hsiao Kuo: Preponderance of the Small.\n
		Preponderance of the Small. Success.
		Perseverance furthers.
		Small things may be done; great things should not be done.
		The flying bird brings the message:
		It is not well to strive upward,
		It is well to remain below.
		Great good fortune.
		"""
	elif hexagram == 63:
		return """
		Chi Chi: After Completion.\n
		After Completion. Success in small matters.
		Perseverance furthers.
		At the beginning good fortune,
		At the end disorder.
		"""
	elif hexagram == 64:
		return """
		Wei Chi: Before Completion.\n
		Before Completion. Success.
		But if the little fox, nearly completing the crossing,
		Gets his tail in the water,
		There is nothing that would further.
		"""
	
	
def getImage(hexagram):
	if hexagram == 1:
		return """
		The movement of heaven is full of power.
		Thus the superior man makes himself strong and untiring.
		"""
	elif hexagram == 2:
		return """
		The earth\'s condition is receptive devotion.
		Thus the superior man who has breadth of character
		Carries the outer world.
		"""
	elif hexagram == 3:
		return """
		Clouds and thunder:
		The image of Difficulty at the Beginning.
		Thus the superior man
		Brings order out of confusion.
		"""
	elif hexagram == 4:
		return """
		A spring wells up at the foot of the mountain:
		The image of Youth.
		Thus the superior man fosters his character
		By thoroughness in all that he does.
		"""
	elif hexagram == 5:
		return """
		Clouds rise up to heaven:
		The image of Waiting.
		Thus the superior man eats and drinks,
		Is joyous and of good cheer.
		"""
	elif hexagram == 6:
		return """
		Heaven and water go their opposite ways:
		The image of Conflict.
		Thus in all his transactions the superior man
		Carefully considers the beginning.
		"""
	elif hexagram == 7:
		return """
		In the middle of the earth is water:
		The image of the Army.
		Thus the superior man increases his masses
		By generosity toward the people.
		"""
	elif hexagram == 8:
		return """
		On the earth is water:
		The image of Holding Together.
		Thus the kings of antiquity
		Bestowed the different states as fiefs
		And cultivated friendly relations
		With the feudal lords.
		"""
	elif hexagram == 9:
		return """
		The wind drives across heaven:
		The image of the Taming Power of the Small.
		Thus the superior man
		Refines the outward aspect of his nature.
		"""
	elif hexagram == 10:
		return """
		Heaven above, the lake below:
		The image of Treading.
		Thus the superior man discriminates between high and low,
		And thereby fortifies the thinking of the people.
		"""
	elif hexagram == 11:
		return """
		Heaven and earth unite: the image of Peace.
		Thus the ruler
		Divides and completes the course of heaven and earth;
		He furthers and regulates the gifts of heaven and earth,
		And so aids the people.
		"""
	elif hexagram == 12:
		return """
		Heaven and earth do not unite:
		The image of Standstill.
		Thus the superior man falls back upon his inner worth
		In order to escape the difficulties.
		He does not permit himself to be honored with revenue.
		"""
	elif hexagram == 13:
		return """
		Heaven together with fire:
		The image of Fellowship with Men.
		Thus the superior man organizes the clans
		And makes distinctions between things.
		"""
	elif hexagram == 14:
		return """
		Fire in heaven above:
		The image of Possession in Great Measure.
		Thus the superior man curbs evil and furthers good,
		And thereby obeys the benevolent will of heaven.
		"""
	elif hexagram == 15:
		return """
		Within the earth, a mountain:
		The image of Modesty.
		Thus the superior man reduces that which is too much,
		And augments that which is too little.
		He weighs things and makes them equal.
		"""
	elif hexagram == 16:
		return """
		Thunder comes resounding out of the earth:
		The image of Enthusiasm.
		Thus the ancient kings made music
		In order to honor merit,
		And offered it with splendor
		To the Supreme Deity,
		Inviting their ancestors to be present.
		"""
	elif hexagram == 17:
		return """
		Thunder in the middle of the lake:
		The image of Following.
		Thus the superior man at nightfall
		Goes indoors for rest and recuperation.
		"""
	elif hexagram == 18:
		return """
		The wind blows low on the mountain:
		The image of Decay.
		Thus the superior man stirs up the people
		And strengthens their spirit.
		"""
	elif hexagram == 19:
		return """
		The earth above the lake:
		The image of Approach.
		Thus the superior man is inexhaustible
		In his will to teach,
		And without limits
		In his tolerance and protection of the people.
		"""
	elif hexagram == 20:
		return """
		The wind blows over the earth:
		The image of Contemplation.
		Thus the kings of old visited the regions of the world,
		Contemplated the people,
		And gave them instruction.
		"""
	elif hexagram == 21:
		return """
		Thunder and lightning:
		The image of Biting Through.
		Thus the kings of former times made firm the laws
		Through clearly defined penalties.
		"""
	elif hexagram == 22:
		return """
		Fire at the foot of the mountain:
		The image of Grace.
		Thus does the superior man proceed
		When clearing up current affairs.
		But he dare not decide controversial issues in this way.
		"""
	elif hexagram == 23:
		return """
		The mountain rests on the earth:
		The image of Splitting Apart.
		Thus those above can ensure their position
		Only by giving generously to those below.
		"""
	elif hexagram == 24:
		return """
		Thunder within the earth:
		The image of the Turning Point.
		Thus the kings of antiquity closed the passes
		At the time of solstice.
		Merchants and strangers did not go about,
		And the ruler
		Did not travel through the provinces.
		"""
	elif hexagram == 25:
		return """
		Under heaven thunder rolls:
		All things attain the natural state of innocence.
		Thus the kings of old,
		Rich in virtue, and in harmony with the time,
		Fostered and nourished all beings.
		"""
	elif hexagram == 26:
		return """
		Heaven within the mountain:
		The image of the Taming Power of the Great.
		Thus the superior man acquaints himself with many sayings of antiquity
		And many deeds of the past,
		In order to strengthen his character thereby.
		"""
	elif hexagram == 27:
		return """
		At the foot of the mountain, thunder:
		The image of Providing Nourishment.
		Thus the superior man is careful of his words
		And temperate in eating and drinking.
		"""
	elif hexagram == 28:
		return """
		The lake rises above the trees:
		The image of Preponderance of the Great.
		Thus the superior man, when he stands alone,
		Is unconcerned,
		And if he has to renounce the world,
		He is undaunted.
		"""
	elif hexagram == 29:
		return """
		Water flows on uninterruptedly and reaches its goal:
		The image of the Abysmal repeated.
		Thus the superior man walks in lasting virtue
		And carries on the business of teaching.
		"""
	elif hexagram == 30:
		return """
		That which is bright rises twice:
		The image of Fire.
		Thus the great man, by perpetuating this brightness,
		Illumines the four quarters of the world.
		"""
	elif hexagram == 31:
		return """
		A lake on the mountains:
		The image of Influence.
		Thus the superior man encourages people to approach him
		By his readiness to receive them.
		"""
	elif hexagram == 32:
		return """
		Thunder and wind: the image of Duration.
		Thus the superior man stands firm
		And does not change his direction.
		"""
	elif hexagram == 33:
		return """
		Mountain under heaven: the image of Retreat.
		Thus the superior man keeps the inferior man at a distance,
		Not angrily but with reserve.
		"""
	elif hexagram == 34:
		return """
		Thunder in heaven above:
		The image of the Power of the Great.
		Thus the superior man does not tread upon paths
		That do not accord with established order.
		"""
	elif hexagram == 35:
		return """
		The sun rises over the earth:
		The image of Progress.
		Thus the superior man himself
		Brightens his bright virtue.
		"""
	elif hexagram == 36:
		return """
		The light has sunk into the earth:
		The image of Darkening of the Light.
		Thus does the superior man live with the great mass:
		He veils his light, yet still shines.
		"""
	elif hexagram == 37:
		return """
		Wind comes forth from fire:
		The image of the Family.
		Thus the superior man has substance in his words
		And duration in his way of life.
		"""
	elif hexagram == 38:
		return """
		Above, fire; below, the lake:
		The image of Opposition.
		Thus amid all fellowship
		The superior man retains his individuality.
		"""
	elif hexagram == 39:
		return """
		Water on the mountain:
		The image of Obstruction.
		Thus the superior man turns his attention to himself
		And molds his character.
		"""
	elif hexagram == 40:
		return """
		Thunder and rain set in:
		The image of Deliverance.
		Thus the superior man pardons mistakes
		And forgives misdeeds.
		"""
	elif hexagram == 41:
		return """
		At the foot of the mountain, the lake:
		The image of Decrease.
		Thus the superior man controls his anger
		And restrains his instincts.
		"""
	elif hexagram == 42:
		return """
		Wind and thunder: the image of Increase.
		Thus the superior man:
		If he sees good, he imitates it;
		If he has faults, he rids himself of them.
		"""
	elif hexagram == 43:
		return """
		The lake has risen up to heaven:
		The image of Break-through.
		Thus the superior man 
		Dispenses riches downward
		And refrains from resting on his virtue.
		"""
	elif hexagram == 44:
		return """
		Under heaven, wind:
		The image of Coming to Meet.
		Thus does the prince act when disseminating his commands
		And proclaiming them to the four quarters of heaven.
		"""
	elif hexagram == 45:
		return """
		Over the earth, the lake:
		The image of Gathering Together.
		Thus the superior man renews his weapons
		In order to meet the unforeseen.
		"""
	elif hexagram == 46:
		return """
		Within the earth, wood grows:
		The image of Pushing Upward.
		Thus the superior man of devoted character
		Heaps up small things
		In order to achieve something high and great.
		"""
	elif hexagram == 47:
		return """
		There is no water in the lake:
		The image of Exhaustion.
		Thus the superior man stakes his life
		On following his will.
		"""
	elif hexagram == 48:
		return """
		Water over wood: the image of the Well.
		Thus the superior man encourages the people at their work,
		And exhorts them to help one another.
		"""
	elif hexagram == 49:
		return """
		Fire in the lake: the image of Revolution.
		Thus the superior man
		Sets the calendar in order
		And makes the seasons clear.
		"""
	elif hexagram == 50:
		return """
		Fire over wood:
		The image of the Caldron.
		Thus the superior man consolidates his fate
		By making his position correct.
		"""
	elif hexagram == 51:
		return """
		Thunder repeated: the image of Shock.
		Thus in fear and trembling
		The superior man sets his life in order
		And examines himself.
		"""
	elif hexagram == 52:
		return """
		Mountains standing close together:
		The image of Keeping Still.
		Thus the superior man
		Does not permit his thoughts
		To go beyond his situation.
		"""
	elif hexagram == 53:
		return """
		On the mountain, a tree:
		The image of Development.
		Thus the superior man abides in dignity and virtue,
		In order to improve the mores.
		"""
	elif hexagram == 54:
		return """
		Thunder over the lake:
		The image of the Marrying Maiden.
		Thus the superior man
		Understands the transitory
		In the light of the eternity of the end.
		"""
	elif hexagram == 55:
		return """
		Both thunder and lightning come:
		The image of Abundance.
		Thus the superior man decides lawsuits
		And carries out punishments.
		"""
	elif hexagram == 56:
		return """
		Fire on the mountain:
		The image of the Wanderer.
		Thus the superior man
		Is clear-minded and cautious
		In imposing penalties,
		And protracts no lawsuits.
		"""
	elif hexagram == 57:
		return """
		Winds following one upon the other:
		The image of the Gently Penetrating.
		Thus the superior man
		Spreads his commands abroad
		And carries out his undertakings.
		"""
	elif hexagram == 58:
		return """
		Lakes resting one on the other:
		The image of the Joyous.
		Thus the superior man joins with his friends
		For discussion and practice.
		"""
	elif hexagram == 59:
		return """
		The wind driven over the water:
		The image of Dispersion.
		Thus the kings of old sacrificed to the Lord
		And built temples.
		"""
	elif hexagram == 60:
		return """
		Water over lake: the image of Limitation.
		Thus the superior man
		Creates number and measure,
		And examines the nature of virtue and correct conduct.
		"""
	elif hexagram == 61:
		return """
		Wind over lake: the image of Inner Truth.
		Thus the superior man discusses criminal cases
		In order to delay executions.
		"""
	elif hexagram == 62:
		return """
		Thunder on the mountain:
		The image of Preponderance of the Small.
		Thus in his conduct the superior man gives preponderance to reverence.
		In bereavement he gives preponderance to grief.
		In his expenditures he gives preponderance to thrift.
		"""
	elif hexagram == 63:
		return """
		Water over fire: the image of the condition
		In After Completion.
		Thus the superior man
		Takes thought of misfortune
		And arms himself against it in advance.
		"""
	elif hexagram == 64:
		return """
		Fire over water:
		The image of the condition before transition.
		Thus the superior man is careful
		In the differentiation of things,
		So that each finds its place.
		"""

		
r = random.randint(1, 13)
judgment = getJudgment(r)
image = getImage(r)
print(judgment)
print(image)

		


