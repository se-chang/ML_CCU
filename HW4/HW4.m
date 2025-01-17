clear;
clc;
train_X = csvread('train.csv');
train_y = csvread('label.csv');
test_X = csvread('test.csv');
%test_y = csvread('Test_label.csv');
test_y = zeros(3283,1);
model = svmtrain(train_y, train_X, '-b 1 -t 3 -m 10000');
[predict_label, accuracy, dec_values] = svmpredict(test_y, test_X, model, '-b 1');
output = dec_values(:,2);
csvwrite("submission.csv",output);