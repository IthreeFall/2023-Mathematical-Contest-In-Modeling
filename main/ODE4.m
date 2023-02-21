function [t,y,n]=ODE4(ufunc,tspan,y0,h)%参数表顺序依次是微分方程组的函数名称，时间起点终点,初始值，步长（参数形式参考了ode45函数）
if nargin<4
    h=0.01;
end
if size(tspan)==[1,2]
    t0=tspan(1);
    tn=tspan(2);
else
    error(message('MATLAB:runge_kuttx0_o4:WrongDimensionOfTspan'));
end
n=floor((tn-t0)/h);%求步数
t(1)=t0;%时间起点
y(:,1)=y0;%第一列赋初值，可以是向量，代表不同的初始值
for i=1:n
t(i+1)=t(i)+h;
k1=ufunc(t(i),y(:,i));
k2=ufunc(t(i)+h/2,y(:,i)+h*k1/2);
k3=ufunc(t(i)+h/2,y(:,i)+h*k2/2);
k4=ufunc(t(i)+h,y(:,i)+h*k3);
y(:,i+1)=y(:,i)+h*(k1+2*k2+2*k3+k4)/6;
%按照龙格库塔方法进行数值求解
end
