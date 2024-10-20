import re
import pandas as pd

# Sample input text (replace this with your actual text)
text = """"
1017/1018 - The Last One
Written by: Marta Kauffman & David Crane
Directed by: Kevin Bright
Transcribed by: Kreidy

[Scene: Monica and Chandler's apartment. It's a scene from 1016 TOW Rachel's Going Away Party.]

Jennifer Aniston (V.O.): Previously on Friends.

Monica: Erica, are you okay?

Erica: Yeah, you know, maybe I ate too much. I keep getting these stomach-aches. They come and go like every few minutes.

Monica: Oh my God!

Chandler: Relax! We'll just get her some antacids.

Monica: She doesn't have a stomach-ache. She's in labor!

Chandler: Oh my God!

 

[Cut to Ross's apartment. Ross and Rachel are there. It's another scene from 1016 TOW Rachel's Going Away Party.]

Rachel: So if you think I didn't say goodbye to you because you don't mean as much to me as everybody else, you're wrong. It's because you mean more to me.

Ross: Rach!

Rachel: What?!

(He walks over and kisses her. They pull back, Rachel looks at him, and they kiss again.)

 

[Scene: Ross's bedroom. Rachel is putting on her shoes as Ross shows up from underneath the covers.]

Ross: Hey.

Rachel: Shh.. Go back to sleep. I have to go home.

Ross: Oh. This was amazing.

Rachel: It really was. You've learned some new moves!

Ross: Yeah, well, this guy at work gave me "Sex for Dummies" as a joke.

Rachel: Ah.

Ross: Who's laughing now?

Rachel: I know!

(They kiss.)

 

OPENING CREDITS

[Scene: The delivery room at the hospital. Monica, Chandler and Erica are there. Erica is in labor, and she is breathing heavily.]

Monica: Breathe, breathe, breathe... Good.

Chandler: Next time, can I say breathe?

Monica: No, last time you said it like Dracula, and it scared her! Can I get you anything? You want some more ice chips?

Erica: No, I'm okay.

Monica: Alright, I'll be right back.

Chandler: Where are you going?

Monica: To use the bathroom.

Chandler: You can't leave me alone with her.

Monica: What?

Chandler: This is exactly the kind of social situation that I am not comfortable with!

Monica: What kind of social situation are you comfortable with?

Chandler: It's just that we've never spent any time, you know, alone together.

Monica: You'll be fine. Nah, you won't, but I'll be back in two minutes.

Chandler: Okay.

(Monica leaves, and Chandler closes the door. Erica just looks at him.)

Chandler: So, ah... Any plans for the summer?

Erica: I don't know. Maybe church-camp?

Chandler: Hah. May not wanna mention this. So, you ever wonder which is worse, you know; going through labor or getting kicked in the nuts?

Erica: What?

Chandler: Well, it's just interesting. You know, because no one will ever know, because no one can experience both.

(Erica just looks at him like he's crazy.)

Chandler: One of life's great, unanswerable questions. I mean, who knows? Maybe there's something even more painful than those things? Like this.

 

[Scene: Joey and Rachel's apartment. Joey is there as Phoebe enters. Joey is holding a baby duck.]

Phoebe: Morning.

Joey: Hey!

Phoebe: What's that?

Joey: It's my house-warming present for Monica and Chandler.

Phoebe: It's a baby chick and duck!

Joey: Uh-huh. And I named them Chick Jr. and Duck Jr.

Phoebe: I did not see that coming.

Joey: Yeah, I figure they'll love it at the new house, you know? It has that big backyard. And then, when they get old, they can go to that special farm that Chandler took the other chick and duck to.

Phoebe: Yes.

Joey: Yeah. It's a shame people can't visit there.

Phoebe: That is the rule, though.

(Ross enters.)

Phoebe: Guess what? You're almost an uncle!

Ross: What?

Joey: Yeah, Erica went into labor last night. Monica and Chandler are at the hospital right now!

Ross: Oh my God!

Phoebe: Yeah, and I have a definite feeling it's gonna be a girl.

Ross: Phoebe, you were sure Ben was gonna be a girl.

Phoebe: Have you seen him throw a ball?

Ross: Is Rachel here?

Joey: Uh, I think she's still asleep. Hey, hey, how did it go with you guys last night? She seemed pretty pissed at you.

Ross: Uh, we, y'know, we worked things out.

Phoebe: What's that smile? Did something happen with you two?

Ross: Hey, I'm not one to kiss and tell, but I'm also not one to have sex and shut up. We totally did it!

Joey: Oh my God. You and Rachel?

Ross: I know, it's pretty great.

Joey: So what does that mean? Are you guys getting back together?

Ross: Oh, I.. I don't know. We didn't really get to talk.

Phoebe: But do you wanna get back together?

Ross: I don't know. It was incredible. I mean, it just felt so right. When I was holding her, I mean, I never wanted to let her go. You know what? Yeah, I do. I wanna be together.

Phoebe: (screaming) YAY!

Ross: Shhh!

Phoebe: (quietly) Yay!

Joey: So, so is she still going to Paris?

Ross: Wow, I hadn't thought of that. I hope not.

Phoebe: Oh, this is like the best day ever. Ever! You guys might get back together, Monica and Chandler are getting their baby, there are chicks and ducks in the world again! Oh, I feel like I'm in a musical! (Singing) "Daa - raa... When the sun comes up, bright and beaming! And the moon comes..."

(Rachel enters from her room.)

Rachel: Morning!

Phoebe: Guess we'll never know how it ends.

Joey: Okay.

Ross: Hey.

Rachel: Hey.

Ross: Hey. How did you sleep?

Rachel: Good. You?

Ross: Good.

Joey: I bet you did!

Ross: Uh. Would you guys mind giving us a minute?

Joey: Sure, yeah. Will you just keep an eye on the chick and the duck?

Rachel: Chick and the duck? Didn't they die...

Phoebe: (interrupting) Dive. Yeah, they dove head-first into fun on the farm.

(Joey and Phoebe leave.)

Ross: So...

(He kisses her.)

Ross: Morning.

Rachel: You too. Last night was just wonderful.

Ross: It really was.

Rachel: I woke up today with the biggest smile on my face.

Ross: I know, me too. It was... You know, it was like one of those things you think is never gonna happen, and then it does, and it's everything you want it to be.

Rachel: Uh-huh. I know. It was just, it was just the perfect way to say goodbye. (She hugs him, and Ross looks crushed.)

 

[Scene: The Hospital. Erica is moaning and about to give birth. Monica, Chandler, a nurse and a doctor are there with her.]

Monica: It's just a little bit more, honey.

Erica: Help me! This hurts!

Chandler: Is it really that bad?

Erica: Uh-huh! I think it's time to kick you in the nuts and see which is worse!

(Monica gives Chandler a look.)

Doctor: The baby's head is crowning.

(Monica walks down to Erica's legs to watch the birth.)

Monica: Oh! Oh my God! That is the most beautiful top of a head I have ever seen! Chandler, you have to see this!

(Chandler is standing by Erica's head.)

Chandler: I'm okay.

Monica: Chandler, you don't wanna miss this. This is the birth of your child! It's the miracle of life!

Chandler: Alright. Wow, that is one disgusting miracle.

Doctor: Start pushing. Here we go. Here come the shoulders...

(The baby starts crying, and the doctor holds it up.)

Monica: It's a... It's a boy!

Chandler: Wow!

Erica: Is he okay?

Doctor: He's just fine.

Monica: Oh, you did it!

Chandler: (emotional) It's a baby! A beautiful little baby! And some other stuff I'm gonna pretend I don't see.

Doctor: Would you like to cut the umbilical cord?

(A nurse gives Monica a pair of scissors. Monica gives it to Chandler, and they cut it together.)

Chandler: Well, that's spongy.

Monica: (to her son) Oh, hey handsome! Oh, I'm gonna love you so much that no woman is ever gonna be good enough for you! (To Chandler, on the verge of tears) Oh, we are so lucky!

Chandler: I know. He has your eyes.

(Monica looks at him.)

Chandler: I mean, I know that's not possible, but he does.

Nurse: We'll just get him cleaned up a bit.

(The doctor hands the boy to the nurse, and she walks over to another part of the room with him.)

Chandler: Okay.

Monica: (To Erica) Oh my God, he's beautiful. Thank you so much.

Erica: I'm really happy for you guys.

Chandler: How do you feel?

Erica: I'm tired!

Doctor: Well, you don't have that much time to relax. The other one will be along in a minute.

(Chandler stares at the doctor, completely shocked. Monica just freezes and turns around slowly.)

Monica: I... I'm sorry, who should be along in a what now?

Doctor: The next baby should be along in a minute.

Monica: We only ordered one!

Doctor: You know it's twins, right?

Chandler: Oh, yeah! These are the faces of two people in the know!

COMMERCIAL BREAK

[Scene: The hospital. Continued from earlier.]

Doctor: I can't believe you didn't know it's twins! This has never happened before.

Chandler: Well, gosh. That makes me feel so special and good.

Monica: (to the doctor) Wait, did you know it was twins?

Doctor: Yeah, it's here in the paperwork we got from the clinic in Ohio.

Monica: (to Erica) Anybody tell you?

Erica: I don't think so. Although, they did mention something about two heartbeats. But I thought that was just mine and the baby's. They kept saying both heartbeats are really strong, and I thought well, that's good 'cause I'm having a baby.

Monica: This is unbelievable.

Erica: Twins actually run in my family.

Chandler: Interesting! (To Monica) Can I see you for a second?

(They walk over to the door.)

Chandler: What do we do?

Monica: What do you mean "what do we do"?

Chandler: (panicking) Twins! Twins!!

Monica: Chandler, you're panicking!

Chandler: Uh-huh! Join me, won't you?! Okay, what do you say we keep one, and then just like have an option on the other one?

Monica: We can't split them up!

Chandler: Why not? We could give each of them half a medallion, and then years later, they'll find each other and be reunited. I mean, that's a great day for everybody.

Monica: Okay, what if the person who adopts the other one is horrible?

Chandler: What if they're not? What if it's adopted by a king?

Monica: Yeah, because I hear the king is looking to adopt.

Chandler: Monica, we are not ready to have two babies!

Monica: That doesn't matter! We have waited so long for this. I don't care if it's two babies. I don't care if it's three babies! I don't care if the entire cast of "Eight is Enough" comes out of there! We are taking them home, because they are our children!

Chandler: (smiles) Okay. Shhh...

(He hugs her.)

Chandler: Okay.

Monica: Okay!

Chandler: Okay!

Doctor: It looks like we're about ready over here.

(Monica and Chandler run back to Erica's bed.)

Doctor: Come on, Erica, start pushing again now.

Erica: Ow!

(Erica screams.)

Doctor: Here she comes!

Chandler: (shocked) She? It's a girl?

Doctor: Yeah.

Chandler: (To Monica) Well, now we have one of each! (To the doctor) And that's enough!

 

[Scene: Central Perk. Ross, Phoebe and Joey are there.]

Ross: And then she said it was the perfect way to say goodbye.

Joey: Oh my God! What did you say?

Ross: Nothing! What do you say to that?

Phoebe: Ross, you've got to tell her how you feel!

Ross: No way!

Joey: You can't just give up! Is that what a dinosaur would do?

Ross: What?

Joey: Dude, I'm just trying to speak your language.

Phoebe: Ross, Rachel doesn't know that you wanna get back together. If she did, she might feel differently. She might not even go.

Ross: You really think so?

Phoebe: I'm telling you! Oh, okay! This is the part of the musical where there'd be a really good convincing song. (Singing) "Bam-bam, don't take no for an answer. Bam-bam, don't let love fly away. Bam-bam-bam-bam..."

(Rachel enters and interrupts Phoebe's song.)

Rachel: Hi!

Phoebe: Can't a girl finish a song around here?

Joey: Hey!

Rachel: Hi! So I just dropped Emma off at my mom's.

Ross: Okay.

Joey: Oh, you're not taking her with you tonight?

Rachel: No, we decided that I would go ahead and set up first, and then my mom would bring Emma to Paris on Sunday.

Phoebe: Wow, eight hour flight with a one-year old? Good luck, mom.

Rachel: Are you kidding? Eight hours with my mother talking about Atkins? Good luck, Emma!

(Rachel walks up to the counter.)

Ross: Alright, you know what? You're right. I should at least tell her how I feel.

(He stands up.)

Joey: Ross, wait!

Ross: What? What?

Joey: Could you get me a muffin?

(Ross walks up to Rachel, but Gunther gets there first.)

Gunther: Rachel?

Rachel: Yeah?

Gunther: I... I know you're leaving tonight, but I just have to tell you. I love you.

(Ross is shocked.)

Gunther: I... I don't know if that changes your plans at all, but I thought you should know.

Rachel: (touched) Gunther... Oh... I love you too. Probably not in the same way, but I do. And, and when I'm in a café, having coffee, or I see a man with hair brighter than the sun, I'll think of you. Aw.

(She kisses him on the cheek and looks over at the others.)

Rachel: Oh... Bye guys.

(Rachel leaves.)

Ross: Oh my God!

Phoebe: Unbelievable!

Joey: Hey, you know what might help?

Ross: I'm not getting you a muffin!

 

[Scene: The hospital. Monica and Chandler are holding the twins, while two nurses are taking care of Erica.]

Monica: Do you think they recognize each other from in there?

Chandler: Maybe. Unless they're like two people who have lived in apartments next to each other for years, and then one day they're pushed through a vagina and they meet.

Nurse: We're going to take Erica to recovery now.

Monica: There's something that we wanna tell you. We decided to name the girl-baby Erica.

Erica: Oh my God, that's just like my name!

Monica: Son of a gun, it is!

Erica: Anyway, I'm gonna go and get some rest. I'm really glad I picked you guys. You're gonna make great parents. Even Chandler.

Monica: Okay, well, bye!

Erica: Bye!

Chandler: Bye!

Monica: We'll call you!

Erica: Okay.

Chandler: Have fun at church-camp!

(The nurses take Erica to the recovery room. Monica and Chandler smile at each other.)

Monica: Oh, look at these little bunnies!

Chandler: I know! You ready to trade?

Monica: Okay.

Chandler: Okay.

Monica: Alright, let's see..

(They start trying to trade babies while holding one each. They have no idea how to do it, so they just shift the babies around in their arms. They give up pretty quickly.)

Chandler: We could trade later.

Monica: Yeah, I'm good.

 

[Scene: Monica and Chandler's apartment. Joey and Phoebe are there. There is a white crib decorated with balloons in the middle of the apartment. Also, there are boxes all over the apartment. Joey is working on something on the coffee table.]

Phoebe: Hey, what are you working on?

Joey: It's a... It's a "welcome home" sign for the baby.

(He holds up a white poster with huge red letters. It reads, "Welcome Home Baby." There is also a huge red stain on the left of the poster.)

Phoebe: How sweet! Oh, is that the baby?

(She points at the stain.)

Joey: No, I sat in the paint.

(Ross enters with a gift for the baby.)

Ross: Hey.

Phoebe: Hey. So, did you talk to Rachel?

Ross: No, and I'm not going to.

Phoebe: What?

Joey: Why not?

Ross: Because she's just going to shoot me down. You guys saw what happened with Gunther. That did not look like fun.

Phoebe: How can you compare yourself to Gunther? I mean, sure, he's sexy in a more obvious way. You have a relationship with her, you slept together last night.

Ross: Yeah, and she still wants to go! It's pretty clear where she is.

Joey: Yeah, I know what you mean. I mean, sometimes...

(He sits down in the wet paint again.)

Phoebe: Uh, Joe?

Joey: Damn it!

Ross: Look, even if I were gonna tell her, I don't have to do it now. Okay? I'll be seeing her again. We've got time.

Phoebe: No, you don't! She's going to Paris! She is going to meet somebody. Do you know how many hot guys there are in Paris? It's... It's a city of Gunthers!

(Mike enters with a roll of paper in his hand.)

Mike: Hey!

Phoebe: Hey! What do you have there?

Mike: Oh, I made a little something. If I had more time to work on it, it'd be better, but..

(He shows them a beautiful banner he has made. It reads, "Welcome to the World, Baby Bing.")

Ross: Oh my God! You did that yourself?

Phoebe: Honey, that's gorgeous!

Joey: You know, the baby can't read, Mike!

(Rachel enters.)

Rachel: Hi! You guys, the car-service just got here. I can't believe they're not home yet! I have to catch my stupid plane. I wanna see the baby!

Joey: Monica just called from the cab. She said they should be here any minute. And apparently, there's some big surprise.

Phoebe: Yeah, did she sound happy about it? 'Cause my friend Ethel's baby was born with a teeny, tiny beard.

(Monica enters carrying her son.)

Rachel: Oh my God!

Ross: Oh my God!

(They all walk over to see the baby.)

Rachel: Hi! Oh my gosh!

(Chandler enters carrying his daughter.)

Chandler: Hey.

(Everybody turns around.)

Phoebe, Ross, Rachel: Hey.

(They turn back around to see the baby Monica's carrying, but then they realise what the surprise is. Ross, Mike, Phoebe and Rachel gasp and stare at Chandler and his baby. Joey hasn't figured it out yet.)

Joey: (To Monica) Hey, so what is the big surprise?

Rachel: Oh.

(Joey stares at Chandler and Monica and finally puts two and two together. He gasps.)

Ross: Oh my God!

Rachel: What... What...

Ross: Okay, okay, awkward question. The hospital knows you took two, right?

Monica: Yes, it's twins!

Ross: Oh my God.

Joey: Oh, they're so cute! Now, what, what kinds are they?

Monica: (points at the baby she's holding) This is a boy, (points at the baby Chandler is holding) and that's a girl.

Chandler: Her name is Erica.

Rachel: Aw..

Joey: Hey, that pregnant girl's name was Erica.

Chandler: Yeah. It's a shame you two didn't get to spend more time together.

Monica: Yeah, we named the boy Jack after dad.

Ross: Aw, he's gonna be so happy.

Phoebe: Oh, Jack Bing. I love that. Ooh, it sounds like a '40s newspaper guy, you know? "Jack Bing, Morning Gazette. I'm gonna blow this story wide open!"

(Chandler and Monica carry Erica and Jack over to the crib and put them down carefully.)

Rachel: Oh my gosh. Wow, so beautiful.

Mike: (To Phoebe) I want one.

Phoebe: Oh yeah? Well, tell me which one, and I'll try slip it in my coat.

Mike: Seriously. Wanna make one of those?

Phoebe: One? How about a whole bunch?

Mike: Really?

Phoebe: Yeah! Ooh, we could teach them to sing, and we can be like the Von Trapp family! Only without the Nazis. Although that sounds kinda dull.

Rachel: Oh, you guys, I can't believe this. But I'll leave now, or I'm gonna miss my plane.

Monica: I'm just so glad you got to see the babies.

(They hug.)

Rachel: Me too. Oh, I'm just sorry I'm not gonna be around to watch you two attempt to handle this! Alright, I can't say goodbye to you guys again. I love you all so much.

Monica: I love you.

Chandler: I love you.

Monica: Call us when you get there.

Rachel: I will. Ross, come here.

(She pulls him over to the door.)

Rachel: I just want you to know.. Last night.. I'll never forget it.

Ross: Neither will I.

(They hug as Phoebe and Joey stare at the two of them.)

Rachel: Alright, now I really have to go. Okay. Au revoir! Oh, they're gonna really hate me over there.

(She leaves.)

Phoebe: So, you just let her go?

Ross: Yeah.

Joey: Hey, maybe that's for the best.

Ross: Yeah?

Joey: Yeah. You know? You just... Look, you gotta... You gotta think about last night the way she does, okay? Maybe, maybe sleeping together was the perfect way to say goodbye?

Phoebe: But now she'll never know how he feels!

Joey: Maybe that's okay. You know? Maybe, maybe it is better this way? I mean, now, now you can move on. I mean, you've been trying to for so long, maybe now that you're on different continents.. (Looks at Phoebe) Right?

(Phoebe nods.)

Joey: Maybe now you can actually do it. You know? You can finally get over her.

Ross: Yeah, that's true. Except I don't wanna get over her.

Joey: What?

Ross: I don't! I wanna be with her.

Joey: Really?

Ross: Yeah, I'm gonna go after her.

Joey: Yeah, you are!

Phoebe: Woo!

(Monica and Chandler look shocked as Ross goes to leave.)

Phoebe: Wait, wait! Get your coat! Get your coat!

Ross: My coat...

Joey: This is so cool!

Chandler: I have no idea what's going on, but I am excited!

Joey: But Ross, Ross. What do you, what do you think she's going to say?

Ross: I don't know, but I.. Look, even if she shoots me down, at least I won't spend the rest of my life wondering what would have happened. Where - where is my coat?!

Phoebe: You didn't bring one! My cab's downstairs, I'll drive you to the airport.

Ross: Okay, guys, wish me luck.

Phoebe: Hurry!

Joey: Good luck, good luck!

(Phoebe and Ross leave.)

 

[Scene: The street right in front of Central Perk. Phoebe's cab is there. Ross and Phoebe run over and jump in.]

Ross: There's no seatbelt!

Phoebe: That's okay. If - if we hit anything, the engine will explode, so you know, it's better if you're thrown from the car.

(Ross looks terrified.)

Ross: Alright, alright, let's do this!

Phoebe: Okay!

(A guy comes up and gets into the backseat of the cab.)

Ross: Hey!

Man: 18th and East End.

Phoebe: I - I don't take passengers.

Man: Hey! The law says you have to accept any fare.

Ross: No, you don't understand. This isn't a real cab.

Man: Alright, I gotta report you. What's your medallion number?

Phoebe: My medallion number is, "Get out of the cab!"

Man: What?

Ross: (screaming) Get out of the cab!

Phoebe: Get out of the cab!

(The man jumps out, obviously a little scared. Phoebe drives off.)

 

[Scene: Monica and Chandler's apartment. Monica, Chandler and Joey are there, packing the last boxes.]

Joey: Oh, hey, hey, can I give you guys your house-warming present now?

Monica: Now, that you can do.

Joey: Alright!

(Cut to Joey's apartment. Joey looks inside the cardboard box that used to be the home of Chick Jr. and Duck Jr., but they have disappeared.)

Joey: Ah... Chick Jr.? Duck Jr.? Don't hide from mama!

 

[Scene: Phoebe's cab. Phoebe is driving very fast, and a terrified Ross has closed his eyes.]

Phoebe: You can open your eyes now.

Ross: Are we off the bridge?

Phoebe: Yes.

Ross: Is the old woman on the bicycle still alive?

Phoebe: Yes, she jumped right back up.

(Ross opens his eyes.)

Ross: Oh my God, Phoebe, slow down!

Phoebe: Do you wanna get to Rachel in time?

Ross: Yes, but I don't wanna die in your cab!

Phoebe: You should have thought of that before you got in!

(They drive up to a toll-booth.)

Phoebe: Toll-booth.

Ross: What?

Phoebe: (screaming) Toll-booth! Four bucks. There are quarters in the glove compartment.

(Ross tries to open a plastic bag filled with quarters, but he's quite slow.)

Phoebe: Hurry!

Ross: Okay!

Phoebe: Okay.

(Phoebe tries to throw some quarters out the window, but she has forgotten to open the window, and she and Ross scream.)

Phoebe: Damn, that window is clean.

 

[Scene: Joey's apartment. Joey is still looking for the birds.]

Joey: Quack, quack, tweet, tweet, quack, quack, tweet, tweet, quack, quack, tweet, tweet, quack, quack, tweet, tweet, quack, tweet, quack...

(Monica and Chandler enter.)

Chandler: We were wondering what was taking so long with the gift, but now we understand you were doing this.

Joey: Okay, I wanted to surprise you, but for your house-warming gift, I got you a baby-chick and a baby-duck!

(Chandler grins, while Monica is less enthusiastic.)

Chandler: Really? You got us a chick and a duck?

Monica: Oh, great! Just what you want for a new house with infants. Bird feces.

Joey: Yeah, yeah, they must have jumped off the table, 'cause now they're gone!

Chandler: Oh, don't worry, we'll find them.

Monica: Actually, I'm gonna go check on the twins.

Chandler: Alright.

(Monica turns around and is about to leave when she steps on something.)

Monica: Oh God! What did I just step on?

Joey: Oh!

Chandler: It's okay, it's just an egg roll.

Monica: Oh..

Joey: You stepped on my egg roll?

Monica: I'm sorry, I didn't know to look for Chinese food on the floor.

Joey: Just put it on a plate and leave.

(She does so.)

Chandler: Okay, let's find these birds.

Joey: Alright.

(Suddenly, they hear the birds.)

Joey: Wait, wait. Do you hear that?

(They realise that the birds are in the foosball table.)

Joey: Oh! They're in the table!

Chandler: Well, that can't be good!

Joey: We gotta get them out of there!

Chandler: How?

Joey: Oh, oh! Maybe we can lure them out. You know any birdcalls?

Chandler: Oh, tons, I'm quite the woodsman.

Joey: Well, maybe we can just tip the table a little.

Chandler: Joey, wait! The ball!

Joey: Oh!

(The ball rolls into one of the goals, and Chandler and Joey listen in horror as the ball makes its way inside the table. Finally, they can hear the birds again.)

Joey: Oh God! So what do we do?

Chandler: I don't know. Maybe we can open this up somehow.

Joey: Okay.

Chandler: No... It's all glued together.

Joey: Does that mean we have to bust it open?

Chandler: I don't know. Maybe.

Joey: Oh my God!

Chandler: I know! It's.. It's the foosball table.

Joey: All right, you know what? We don't have a choice. It's like I would have said in that sci-fi movie if I'd gotten the part. "Those are our men in there, we have to get them out! Even if I have to sacrifice the most important thing in my life; my time-machine."

Chandler: Did that movie ever get made?

Joey: It did not.

 

[Scene: The airport. Ross and Phoebe run in.]

Phoebe: Ross, where are you going?

Ross: To talk to Rachel, isn't that why we took a ride in the death-cab?

Phoebe: What? What are you just gonna walk up to her at the gate? Have you never chased anyone through the airport before?

Ross: Not since my cop-show got cancelled.

Phoebe: You have to get a ticket to get past security.

Ross: What? We're never gonna make it!

Phoebe: Not with that attitude! Now, haul ass!

(They run to the ticket counter, but they get stuck behind a group of old people who are walking very slowly.)

Ross: Okay, if you could all walk slower, that'd be great.

 

[Scene: The gate. Rachel walks up to the man at the gate and gives him her passport.]

Gate attendant #1: (with a French accent) Madame, your passport please?

Rachel: Oh my God! I was so afraid I wasn't gonna remember any of my high-school French, but I understood every word you just said!

Gate attendant #1: Your boarding pass, please.

Rachel: Oh.

(She starts looking through her purse, but she can't find it.)

Rachel: Oh, shoot. I had it. Oh, I can't believe this.

Gate attendant #1: Madame, if you don't have your boarding pass...

Rachel: I have it, I have it, I have it. Oh, okay, I can't find it, but I remember that I was in seat 32C, because that's my bra-size.

Gate attendant #1: Madame, you must have your boarding pass..

Rachel: Okay, fine! But you know what? If I was in 36D, we would not be having this problem.

 

[Scene: The ticket-counter. Ross and Phoebe come running.]

Ross: Hey, I need a ticket.

Phoebe: Just one? I drive you all the way down here, and I don't get to see how it works out?

Ross: Fine, two tickets, I need two tickets.

Phoebe: We're on our honeymoon.

Ticket agent: And the destination?

Ross: I don't care. Whatever is the cheapest.

Phoebe: I'm so lucky I married you.

 

[Scene: The gate. Rachel is still searching for her boarding pass.]

Rachel: Oh! Shoot! Damn it! Where is it? Oh! Oh! I found it! I found it!

(She runs up to the gate and the gate attendant standing there.)

Rachel: Hah! I found it! I told you I would find it! In your face! You're a different person.

 

[Scene: The ticket-counter. Ross and Phoebe have their tickets and start looking at the screens in order to find the gate.]

Ross: Okay, flight 421 to Paris. I don't see it, do you see it?

Phoebe: No, did we miss it?

Ross: No, no, no. That's impossible. It doesn't leave for another 20 minutes.

Phoebe: Maybe we have the flight-number wrong. God.

(Phoebe picks up her cell-phone and calls Monica. Monica is still packing in her apartment.)

Monica: Hello.

Phoebe: Hey, it's me. Here's Ross.

Ross: What? Hey, hey, listen..

(Monica is standing by the crib, and she's looking at her babies.)

Monica: Oh my God! Ross, you wouldn't believe the cute little noises the twins are making. Listen.

(She holds the phone down to the twins.)

Ross: Monica? Monica, Monica, Monica, Monica..?

Monica: Oh, I'm sorry. Shoot, they were doing it before.

Ross: That's alright. Listen, listen.

Monica: Oh, wait, wait, wait! Here they go again.

(She holds down the phone to the twins again.)

Ross: Monica? Monica, Monica, Monica, Monica..?

Monica: Isn't that cute?

Ross: That is precious! Listen! I need Rachel's flight information.

Monica: Oh, okay. Alright, it's flight 421. Leaves at 8:40.

Ross: Yes, that's what I have. It's not on the board.

Monica: That's what it says here. Flight 421, leaves at 8:40, Newark airport.

Ross: What?

Monica: Newark airport. Why, where are you?

Ross: JFK.

(Ross sadly hangs up the phone, while Phoebe looks at him. Cut to Rachel at the gate. She gives her boarding pass to the gate attendant, and she goes onboard. The gate attendant closes the door and locks it.)

 

[Scene: Joey's apartment. Joey and Chandler are still trying to get the birds out of the foosball-table.]

Joey: (yelling) Don't worry, you guys, we're gonna get you out of there.

Chandler: And we're also gonna buy you tiny, bird hearing-aids.

(Joey picks up a hammer and a crowbar and gets ready to destroy the table.)

Joey: Okay. Here goes.

Chandler: What's the matter?

Joey: I need to say goodbye to the table first.

Chandler: I understand.

Joey: Okay. Table, you have given us so many great times. And you guys, Jordan, Victor, Joel... All of you guys. What can I say? You guys make us look good. You wanna say anything?

Chandler: I don't know. Except that, for one last time... (he touches the players as he says the following) Good game, good game, good game, good game, good game, good game, good game.

Joey: Okay, here we go. I can't do it.

Chandler: Well, I can't do it either.

(Monica enters.)

Monica: Hey! Did you find them?

Joey: Yeah, they're stuck inside the table!

Chandler: We have to bust it open, but neither of us can do it!

Monica: Oh, well sure. This gotta be so hard. I'll do it. Gimme!

(Monica grabs the hammer and the crowbar and gets ready to bust it open.)

 

[Scene: Phoebe's cab. She's driving faster than ever before.]

Ross: Phoebe! Wow! No, no, no!

(Phoebe screams.)

Phoebe: Well, I've never gone this fast before.

Ross: Phoebe, forget it, okay? Newark is - is like an hour away. There's no way we're gonna make it in time.

Phoebe: She's got her cell, you could call her.

Ross: I am not doing this over the phone.

Phoebe: You don't have any other choice!

(She lets go of the steering wheel to get her cell-phone from her purse. Ross screams and reaches over in order to hold onto the wheel. Cut to the plane. Rachel is sitting in her seat when her cell-phone rings.)

Rachel: Hello?

Phoebe: Rachel? Oh, good. Hey, by the way, did you just get on the plane?

Rachel: Yeah.

Phoebe: (To Ross) For what it's worth, we would have caught her if we were at the right airport.

Ross: Yay.

Phoebe: Uh, Rach, hang on.

(Phoebe tries to give her phone to Ross, but he won't take it. He mouths "no.")

Rachel: Phoebe? Is everything okay?

Phoebe: Uhm, actually no. No, you've... You have to get off the plane.

Rachel: What? Why?

Phoebe: I have this feeling that something's wrong with it. Something is wrong with the left Philange.

Rachel: Oh, honey, I'm sure there's nothing wrong with the plane.

(The passenger in the seat next to Rachel looks at her and seems a little nervous.)

Rachel: Alright, look, I have to go. I love you, and I will call you the minute I get to Paris.

(Rachel hangs up.)

Passenger #1: Uhm, what was that?

Rachel: Oh, that was just my crazy friend. She told me I should get off the plane, because she had a feeling that there was something wrong with the left Philange.

Passenger #1: Okay, that doesn't sound good.

Rachel: I wouldn't worry about it. She's always coming up with stuff like this, and you know what? She's almost never right.

Passenger #1: But she is sometimes.

Rachel: Well...

(The passenger stands up and gets his suitcase from the overhead compartment.)

Rachel: Wait, what are you doing?

Passenger #1: Well, I can't take this plane now.

Air stewardess: Excuse me, sir, where are you going?

Passenger #1: I have to get off this plane, okay? Her friend has a feeling something's wrong with the left Philange.

Rachel: Could I get some peanuts?

Passenger #2: What's wrong with the plane?

Air stewardess: There's nothing wrong with the plane.

Passenger #1: Yeah! The left Philange!

Air stewardess: There is no Philange!

Passenger #1: Oh my God. This plane doesn't even have a Philange!

Passenger #2: I'm not flying on it!

Air stewardess: Ma'am, please sit down!

Passenger #3: What's going on?

Passenger #1: We're all getting off. There is no Philange!

(Everybody walks out of the plane.)

Rachel: This is ridiculous! I...

(She notices that everybody is leaving.)

Rachel: Yeah, okay.

(Rachel leaves as well.)

 

[Scene: Joey's apartment. Monica has completely destroyed the foosball-table, and Chandler and Joey are holding the birds.]

Monica: Alright. My job here is done.

Chandler: That was... Impressive.

Joey: Yeah, you didn't even use the tools for most of it!

Monica: Yeah, they were just slowing me down. Alright, I have to get back to the babies. I'll see you girls later.

(Monica leaves.)

Chandler: Sorry about the table, man.

Joey: Yeah.

Chandler: You gonna buy a new one?

Joey: Probably not. Nah. I don't know how much I'm gonna wanna play after you go.

Chandler: Well, at least we got these little guys out.

Joey: Yeah.

Chandler: Aww, we were worried about you! Hm. I guess I better get used to things crapping in my hand, huh?

Joey: I'm gonna miss these little guys. It was nice having birds around again.

Chandler: Hey, you know what? Maybe we should keep them here with you.

Joey: What?

Chandler: Yeah, I mean we've got a lot going on right now. And, plus, here they'd have their own room.

Joey: I could get a goose!

Chandler: You know, I - I think you're set with the poultry.

Joey: Thanks man. Did you hear that, you guys? You're gonna get to stay here! And, and it's good, you know, 'cause, 'cause now you have a reason to come visit.

Chandler: I think there may be another reason. So, awkward hug or lame cool guy handshake?

Joey: Uh, lame cool guy handshake, yeah.

(They do the lame cool guy handshake. They look at each other, and then they hug.)

 

[Scene: The gate at the airport. The passengers are standing in line, and they're about to board the plane again.]

Gate attendant #2: Ma'am, I assure you, the plane is fine.

Passenger #2: And you fixed the Philange?

Gate attendant #2: Yes, the Philange is fixed. As a matter of fact, we put a whole lot of extra Philanges onboard, just in case.

(Rachel walks up to the gate. Cut to Ross and Phoebe who come running up to the gate.)

Ross: Where is she?

Phoebe: I don't see her.

Ross: Rachel! Rachel Green!

Phoebe: There she is!

Ross: Rachel! Rachel!

Gate attendant #2: Wow, excuse me, sir, do you have a boarding pass?

Ross: No, no, I just have to talk to someone.

Gate attendant #2: I'm sorry, you cannot go any further without a boarding pass.

Ross: No, no, no, but...

Phoebe: (screaming) RACHEL!!

(Rachel comes back to the gate.)

Rachel: Oh my God... What.. What are you guys doing here?

Phoebe: Okay, you're on.

Rachel: What? What? Ross, you're scaring me. What's going on?

Ross: Okay, the thing is..

Rachel: Yeah?

Ross: Don't go.

Rachel: What?

Ross: Please, please stay with me. I am so in love with you. Please, don't go.

Rachel: Oh my God.

Ross: I know, I know. I shouldn't have waited 'till now to say it, but I'm.. That was stupid, okay? I'm sorry, but I'm telling you now. I love you. Do not get on this plane.

Gate attendant #2: Miss? Are you boarding the plane?

Ross: Hey, hey. I know you love me. I know you do.

Gate attendant #2: Miss?

Rachel: I - I have to get on the plane.

Ross: No, you don't.

Rachel: Yes, I do.

Ross: No, you don't.

Rachel: They're waiting for me, Ross. I can't do this right now, I'm sorry. I'm sorry.

Ross: Rachel?

Rachel: I'm so sorry.

(She boards the plane.)

Ross: I really thought she'd stay.

Phoebe: I'm sorry.

(Phoebe hugs Ross.)

 

[Scene: Monica and Chandler's apartment. Joey, Chandler, Monica and the twins are there. Everything has been put into boxes.]

Monica: Well, that's it. Everything's packed.

Chandler: Wow, this is weird.

Monica: I know.

Joey: Yeah. Uh, does this mean there's nothing to eat?

Monica: I put three lasagnas in your freezer.

Joey: I love you!

(He hugs her. Phoebe enters.)

Joey: Hey!

Phoebe: Hey.

Joey: So did you guys make it in time?

Phoebe: Yeah, yeah, he talked to her, but she got on the plane anyway.

Chandler: Where's Ross?

Phoebe: He went home. He didn't want to see anybody.

 

[Scene: Ross's apartment. Ross enters and checks his messages.]

Rachel: (on the answering machine) Ross, hi. It's me. I just got back on the plane. And I just feel awful. That is so not how I wanted things to end with us. It's just that I wasn't expecting to see you, and all of a sudden you're there and saying these things... And... And now I'm just sitting here and thinking of all the stuff I should have said, and I didn't. I mean, I didn't even get to tell you that I love you too. Because of course I do. I love you. I love you. I love you. What am I doing? I love you! Oh, I've gotta see you. I've gotta get off this plane.

Ross: Oh my God!

Rachel: (on the answering machine) Excuse me?

Air stewardess: (on the answering machine) Miss? Please, sit down!

Rachel: (on the answering machine) I'm sorry. I'm really sorry, but I need to get off the plane, okay? I need to tell someone that I love love them.

Air stewardess: (on the answering machine) Miss, I can't let you off the plane.

Ross: Let her off the plane!

Air stewardess: (on the answering machine) I am afraid you are gonna have to take a seat.

Rachel: (on the answering machine) Oh, please, miss, you don't understand!

Ross: Try to understand!

Rachel: (on the answering machine) Oh, come on, miss, isn't there any way that you can just let me off...

(The message is finished. Ross jumps over to the answering machine.)

Ross: No! No! Oh my God. Did she get off the plane? Did she get off the plane?

Rachel: I got off the plane.

Ross: You got off the plane.

(He walks over and kisses her.)

Rachel: I do love you.

Ross: I love you too, and I'm never letting you go again.

Rachel: Okay. 'Cause this is where I wanna be, okay? No more messing around. I don't wanna mess this up again.

Ross: Me neither, okay? We are - we're done being stupid.

Rachel: Okay. You and me, alright? This is it.

Ross: This is it. Unless we're on a break.

(Rachel gives him a look.)

Ross: Don't make jokes now.

(They kiss again.)

 

[Scene: Monica and Chandler's apartment. Chandler and Monica are holding the twins. Joey and Phoebe are sitting by the window, while Ross and Rachel are standing together. The apartment is completely empty. Two men are carrying a large dresser.]

Monica: Okay, please be careful with that. It was my grandmother's. Be careful.

(Two other men are rolling the big white dog out of the apartment.)

Monica: If that falls off the truck, it wouldn't be the worst thing.

(She slips them some money.)

Ross: Wow.

Rachel: I know. It seems smaller somehow.

Joey: Has it always been purple?

Chandler: (to his children) Look around, you guys. This was your first home. And it was a happy place, filled with love and laughter. But more important, because of rent control, it was a friggin' steal!

(Monica and Chandler put Jack and Erica in their stroller.)

Phoebe: Hey, do you realise that at one time or another we all lived in this apartment?

Monica: Oh, yeah, that's true.

Ross: Uh, I haven't.

Monica: Wait a minute. What about that summer during college that you lived with grandma, and you tried to make it as a dancer?

Ross: Do you realise we almost made it ten years without that coming up?

Monica: Oh, honey, I forgot. I promised Treeger that we'd leave our keys.

Chandler: Oh, okay.

(Chandler and Monica walk over to the kitchen-counter and leave their keys. Then the other four pick out their keys and leave them as well.)

Phoebe: So, I guess this is it.

Joey: Yeah. I guess so.

Monica: (crying) This is harder than I thought it would be.

Chandler: Oh, it's gonna be okay.

(Chandler hugs her. Monica hugs Ross and Rachel as Chandler gets the stroller with the twins.)

Rachel: (crying) Do you guys have to go to the new house right away, or do you have some time?

Monica: We got some time.

Rachel: Okay, should we get some coffee?

Chandler: Sure. Where?

(They all leave the apartment. Joey helps Chandler with the stroller in the hallway, while Monica and Rachel have their arms around each other. Everybody walks downstairs to Central Perk. The camera goes inside the apartment again, and it pans around. We see the keys on the counter, and the final shot is of the frame around the peephole. The screen fades to black.)

THE END

"""

# Regular expression to capture speaker and their dialogue
pattern = r'([A-Za-z]+): (.*?)(?=\n[A-Za-z]+:|\nAll:|\n\[(?:Scene|Customer):|$)'

# Find all matches
matches = re.findall(pattern, text, re.DOTALL)

# Filter out explanations (scenes and actions) that don't belong to a specific character
dialogues = []
for speaker, dialogue in matches:
    if not re.search(r'\[Scene:|Customer:', dialogue):  # Ignore scenes and customer directions
        dialogues.append((speaker.strip(), dialogue.strip()))

# Create a DataFrame
df = pd.DataFrame(dialogues, columns=['Speaker', 'Dialogue'])

# Save to Excel
output_file = 'dataset_transcripts/ep1017.xlsx'
df.to_excel(output_file, index=False)

print(f"Extracted dialogues saved to {output_file}")
