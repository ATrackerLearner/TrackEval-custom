
# TrackEval Custom
*Code for evaluating object tracking.*

All credits go to the [original repo](https://github.com/JonathonLuiten/TrackEval/tree/master/trackeval). This repo is temporary.

***

# How to use this repo

1. Set up a virtual env
2. ``pip install git+https://github.com/ATrackerLearner/TrackEval-custom.git``
3. Get your ground files and tracker results file
4. Show case of what you should do to compute HOTA from two different video sequences. Each sequence has one pair of (gt, tracker_result). So we have (gt1.txt, seq_1.txt) and (gt2.txt, seq_2.txt) file pairs. These files should match [MOT Challenge 2D](https://motchallenge.net/instructions/) criteria 

```
>>> from trackeval import eval_once
>>> d = eval_once(
	"MOT_CHALLENGE_2D",
	["HOTA"],
	[
		["gt1.txt","seq_1.txt"],
		["gt2.txt","seq_2.txt"]
	])
```

***

# Additionnal script ``extract_dict`` and ``print_hota``

Previous package could be considered as standalone. Although, two scripts are included to have a better experience: 
- **``extract_dict``**: Return a list of dictionnaries containing a dictionnary for each (gt,tracker_result) pair. This function has been made because default TrackEval dictionnary is over exhaustive compared to our use of case. So we filtered out to have a light dictionnary with core metrics inside
- **``print_hota``**: Conveniant way to print a HOTA dictionnary which should be from the dictionnary list of ``extract_dict``

So to show up how it would be if both functions are defined in previous python interpreter:

```
>>> d_light = extract_dict(d)
>>> for d_hota in d_light:
>>> |   print_hota(d_hota)
```
