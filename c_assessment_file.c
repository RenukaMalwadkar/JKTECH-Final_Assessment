#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
void Read();
void Write();
struct employee
{
    int id;
    char name[20];
    int salary;
}e[10];
void main()
{
    int ch;
    while(1)
    {
        printf("\n1.Write Data:");
        printf("\n2.Read Data:");
        printf("\n3:STOP Process:");
        printf("\nEnter your choice:");
        scanf("%d",&ch);
        switch(ch)
        {
            case 1:
                Write();
                break;
            case 2:
                Read();
                break;
            case 3:
                exit(1);
            default:
                printf("Wrong Choice");
                break;
        }
}
getch();
}
void Write()
{
    int i,n;
    FILE *fp;
    fp=fopen("information.txt","w");
    if(fp==NULL)
    {
        printf("cant open file");
        getch();
        exit(1);
    }
        printf("Enter How many records you want to store:");
        scanf("%d",&n);
        for(i=0;i<n;i++)
        {
            printf("Enter Employee ID: ");
            scanf("%d",&e[i].id);
            printf("Enter Employee Name: ");
            scanf("%s",e[i].name);
            printf("Enter Employee Salary: ");
            scanf("%d",&e[i].salary);
            fwrite(&e,sizeof(e),1,fp);
        }
fclose(fp);
}
void Read()
{
    FILE *fp;
    fp=fopen("information.txt","r");
    if(fp==NULL)
    {
        printf("Cant Read file contents:");
        getch();
        exit(1);
    }
    int i=0;
    while(fread(&e,sizeof(e),1,fp)==1)
    {
        printf("\nEmployee ID: %d",e[i].id);
        printf("\nEmployee Name: %s",e[i].name);
        printf("\nEmployee Salary: %d",e[i].salary);
        i++;
    }
fclose(fp);
}
