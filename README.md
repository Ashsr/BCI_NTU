# BCI_NTU
A Generic Neurofeedback Training System to improve subjects' performance in BCI experiments
In this project we aim to develop a system based on NF (Neurofeedback) training that can be employed as a prior step of training in various BCI experiment protocols to improve the subject’s brain activity and their BCI performance.
### Procedure/Protocol followed:
The system developed caters to train/modulate Alpha (8-12 Hz) and SMR (12-15Hz) rhythms through simple Graphic User Interfaces, which respond according to their rhythm patterns. The Online BCI system was developed in Python and EEG data was collected from ActiChamp BrainAmp, a 32 electrode EEG amplifier, using Remote Data Access protocol.
#### Alpha Training
Alpha Training consists of 2 sessions. First is training. It consists of one minute of relaxation phase, where the subject is asked to close their eyes and relax. Meanwhile the interface calculates the alpha band power and writes it into a csv file. At the end of a minute, a beep is heard which signals the subject to be ready for Focus training phase. In the focus training phase, a cross is placed at the center and the subject is asked to focus on the cross. The interface calculates the alpha band power and it is mapped to the radius of the circle displayed. If the subject concentrates more, the radius of the circle displayed increases and vice versa. This phase is also a minute long. Next session is the Focus Test Session, where in, in the display, based on the alpha band power of the previous two phases a threshold is calculated and displayed as a red circle. Now the objective for the subject is to focus more on the cross and increase the radius of the green circle beyond the threshold. This session also lasts for a minute.
#### SMR Training
In this training, the subject is presented with a ball and cues for left and right hand movement imagination (5 left and 5 right), the SMR band powers of C3 and C4 are compared and the ball moves accordingly, i.e, it moves right if sufficient difference in band powers is obtained during the right cue and left if sufficient difference in band powers is obtained during the left cue. This session lasts for about 1.5 to 2 minutes.
\n
The interfaces were developed in Python and the code can be found in this repository.
Offline analyses were done in MATLAB.
Code for Gamma and Theta rhythms are yet to be developed.
And main_1 is the primary code and once that is initiated then other sections run smoothly [provided the EEG Head gear is configured properly and all the libraries are installed correctly].
