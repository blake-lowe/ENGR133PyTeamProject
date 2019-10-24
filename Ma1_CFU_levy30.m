%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% ENGR 133 
% Program Description 
This program will return DO concentration using given values and the given equation
%
% Assignment Information
%   Assignment:     Ma1_CFU
ff%   Author:         Christos Levy, levy30@purdue.edu
%   Team ID:        002-10

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%% ____________________
%% INITIALIZATION
DO_sat = 9;
k1 = 0.2;
k2 = 0.4;
t = 14;
L0 = 20;
D0 = 4;



%% ____________________
%% CALCULATIONS
DO = DO_sat-((k1*L0)/(k2-k1))*(exp(-k1*t)-exp(-k2*t))-(D0*exp(-k2*t));

%% ____________________
%% OUTPUTS
fprintf DO

%% ____________________
%% ACADEMIC INTEGRITY STATEMENT
% I have not used source code obtained from any other unauthorized
% source, either modified or unmodified.  Neither have I provided
% access to my code to another. The project I am submitting
% is my own original work.