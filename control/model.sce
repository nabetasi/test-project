function mm=mmodel()
    M=0.36;      //[kg]
    Q=1.19e-4;   //[Hm]
    Z0=3.32e-3;  //[m]
    Zequ=0.005;  //[m]
    Iequ=2.03;   //[A]

    aa=Q*Iequ^2/(M*(Zequ+Z0)^3);
    bb=Q*Iequ/(M*(Zequ+Z0)^2);
    A=[0 1;aa 0]; B=[0;-bb];
    C=[1 0]; D=0;
    mm=syslin('c',A,B,C,D);

endfunction

function pm=pmodel()

    m=0.023;        //[kg]
    Jhat=1.23e-3;   //[kgm^2]
    L=0.2;          //[m]
    myu=2.75e-5;    //[Ns/m]
    zeta=240;
    xi=90;

    p1=m*L/Jhat; p2=myu/Jhat; g=9.81;

    A=[0 0 1 0; 0 0 0 1; 0 0 -zeta 0; 0 p1*g p1*zeta -p2];
    B=[0;0;xi;-p1*xi]
    C=[1 0 0 0; 0 1 0 0];
    pm=syslin('c',A,B,C);
    
endfunction

function bm=bmodel()

    A=[0,1,0,0,0,0;-310.8,-1.763,0,0,0,0;
       0,0,0,1,0,0;0,0,-4.973e3,-1.128,0,0;
       0,0,0,0,0,1;0,0,0,0,-2.518e4,-1.904];
    B=[0;3.651;0;-5.163;0;3.651];
    C=[-8.178,0,-46.26,0,-73.61,0];

    bm=syslin('c',A,B,C);

endfunction