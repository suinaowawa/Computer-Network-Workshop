clear all
close all

%------ Q3.2 ------
data = xlsread('video.csv');
time = data(:,2);

% caculate inter-arrival time
IAT = diff(time);

% min,max,average,standard deviation of IAT
min_IAT = min(IAT);
max_IAT = max(IAT);
average_IAT = mean(IAT);
standard_deviation = std(IAT);
fprintf('The min IAT is %f. The max IAT is %f.\n The average IAT is %f. Standard deviation is %f.\n',min_IAT, max_IAT, average_IAT, standard_deviation);


% instantaneous rate
instantaneous_rate = zeros(88,1);
for i = 1:1:88
    len = sum(sum((time < i)&(time >= i-1)));
    instantaneous_rate(i) = len;
end
figure;
plot(instantaneous_rate)
title('instantaneous rate')

% average rate
average_rate = length(time)/time(end);
fprintf('Average rate is %f.\n',average_rate)

%------Q3.3 -----
% select inter_arrival time smaller than 95-th percentile
threshold = prctile(IAT,95);
clean = IAT(IAT<threshold);

% min,max,average,standard deviation of cleaned data
min_clean = min(clean);
max_clean = max(clean);
average_clean = mean(clean);
standard_deviation_clean = std(clean);
fprintf('The minimum of cleaned data is %f.\nThe maximum of cleaned data is %f.\nThe average of cleaned data is %f.\nThe standard deviation of cleaned data is %f.\n',min_clean, max_clean, average_clean, standard_deviation_clean);


%------Q3.4------
% plot time series of cleaned packets IATS
figure;
plot(clean);
title('Time series of the cleaned packet IATs');
xlabel('n-th packet');
ylabel('inter-arrival time/s');

% plot histogram of the cleaned packet IATS
figure;
histogram(clean)
xlabel('inter-arrival time/s')
ylabel('packet number')
title('histogram of cleaned packet IATs')

%------Q3.5------
% exponential_fit of the time series
mu = expfit(clean);
lamda = 1/mu;
x = 0:0.001:0.015;
PDF = lamda*exp(-lamda*x);
CDF = 1-exp(-lamda*x);
figure;
plot(x,PDF)
title('PDF of exponenial distribution(mu=0.0038)')
figure;
plot(x,CDF)
title('CDF of exponenial distribution(mu=0.0038)')

%-----Q3.6-----
% real distribution and exp fit
figure;
histogram(clean)
hold on
plot(x,PDF)
title('PDF of exponenial distribution(mu=0.0038)and real distribution')
legend('real distribution','exponential fit')
