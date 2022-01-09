#include <stdio.h>
long long D[10001],a,i,j;void main(){int N,Q,q,x,y;scanf("%d%d",&N,&Q);for(;i++<Q;a=0){scanf("%d%d%d",&q,&x,&y);if(q==1)D[x]+=y;else{for(j=x;j<=y;j++)a+=D[j];printf("%lld\n",a);}}}