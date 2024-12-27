# rask-1 
This task involves the writeup of the two questions asked as part of the first taskphase.

## Why do PCBs never have 90 degree turns?
Although the modern etchig process is advanced enough top deal with moat of the limitations of 90 degree etching in PCBs dealing with below MHz signals

Historically these 90 degree has been a bad design choice due to following reasons-

1:- Hindrace to Signal Integrity

90-degree turns lead to impeadance discontinuity. This happens because a 90-degree turn disruption can lead to reflection of the signal( boucing back of the signal like an echo). This happens because 90-degree turns have either a thinner or wider width comapred to the normal trace, thus leading to impeadance discontinuity.

Also due to signal piling up in the 90 degree turn, the signals may also overflow/spill out, interferring with other signals in the pcb(noise spills)

2:- Manufacturing Challenges

During the etching process of a pcb, the resist might blob up or thin out at 90-degree turn leading to an unwanted uneveness in the pcb trace and leading to all kinds of different signal issues.
Also it is usually harder to manufacture sharp 90-degree angles precisely and consistently

Even if one manages to manufacture a precise 90 degree turn, the stress at the sharp corner might lead to formation of cracks at the corner


##### As mentioned before, we have managed to deal with most of these manufacturing and Functional problems due to advancement in our manufacturing and designing process. Keeping all these points in mind is still helpful.
<br><br>

## Why do we use active low when we have active high?
We use an active low signal in place of an active high due to a variety of reasons-

1:- Logic circuits can pick up electrical noise, and noise typically causes small positive voltage spikes.In an active low system, these spikes can be prevented from accidentally trigger a signal, because the system works only when the voltage is low, not when small positive noise is present.

2:- Since we generally use NMOS and NPN transistors, which have default state of High, we use active Low to bring down the state to an ON condition, which is generally easier to bring it up to an on condition using an active high. 
As seen in some microcontroller, we prefer the reset condition to be of the active low state,making it much more reliable and more resistant to your accidental resets due unwanted signal noise.

3:- Interrupt Signals
For systems with interrupt handling, an interrupt pin might be set up as active LOW. 
This means that if an external device needs to alert the controller, it pulls down the interrupt pin  to LOW, signaling that something needs attention.
The default HIGH state ensures that the system runs normally, and the LOW signal only interrupts it when necessary.