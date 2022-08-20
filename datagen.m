load('dataset.mat');
y = dataset(1:319,end);
x = dataset(1:319,1:end-1);
trnData = [x y];
numMFs = 5;
mfType = 'trapmf';
epoch_n = 40;
in_fis = genfis(x,y);
out_fis = anfis(trnData,in_fis,40);   
output = evalfis(dataset(320:end,1:end-1),out_fis);
predicted = abs(round(output)); 
actual = dataset(320:end,end);
figure
plot(stepSize)