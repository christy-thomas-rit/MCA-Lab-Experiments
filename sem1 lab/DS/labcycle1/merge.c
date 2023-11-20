#include<stdio.h>
int merge(int n1,int n2,int a[],int b[],int r[])
{
int i=0,j=0,k=0;
while(i<n1&&j<n2)
{
if(a[i]<b[j])
{
 r[k++]=a[i++];
}
else
{
 r[k++]=b[j++];
}
}
while(i<n1)
{
r[k++]=a[i++];
}
while(j<n2)
{
r[k++]=b[j++];
}

}
int main()
{
int n1,n2;
printf("Enter the size of first array:\n");
scanf("%d",&n1);
int a[n1];
printf("Enter the size of second array:\n");
scanf("%d",&n2);
int b[n2];
int r[n1+n2];
printf("Enter first sorted array:\n");
for(int i=0;i<n1;i++)
{
scanf("%d",&a[i]);
}
printf("Enter second sorted array:\n");
for(int i=0;i<n2;i++)
{
scanf("%d",&b[i]);
}
merge(n1,n2,a,b,r);
printf("sorted array:\n");
for(int i=0;i<n1+n2;i++)
{
printf("%d\n",r[i]);
}
}
