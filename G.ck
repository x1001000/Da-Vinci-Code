// demo2.ck
.1 => dac.gain;

SinOsc oscarray[7];
for(0 => int i; i<7; i++) {
	oscarray[i] => dac;
	Math.pow(2, i) * 97.999 => oscarray[i].freq;
}

1::second => now;