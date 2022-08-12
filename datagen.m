load('dataset.mat');
y = dataset(1:400,end);
x = dataset(1:400,1:end-1);
trnData = [x y];
numMFs = 5;
mfType = 'gauss2mf';
epoch_n = 40;
in_fis = genfis(x,y);
out_fis = anfis(trnData,in_fis,40);   
x_test = [2 1 1 0 1 1]; 

x_test;

output = evalfis(x_test,out_fis);
output;
