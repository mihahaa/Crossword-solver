#include <bits/stdc++.h>
using namespace std;

#define MAXDOTSINROW 8 				//maksimalno tacaka u redu
#define MAXCHANGESBIGGER 10 		//koliko reci hocemo da menjamo za vece table (broj_reci_za_menjanje=ukupan_broj_reci/MAXCHANGESBIGGER)
#define MAXCHANGESSMALLER 3			//koliko reci hocemo da menjamo za manje table
#define LIMITFORBIGGERSMALLER 50	//broj polja u tabli koji je granica za odredjivanje "klase" table (manja ili veca)

vector<vector<char> > charsovi;
int kolkic[105];
string primer;
set<string> strings;
vector<string> reci;
vector<string> reciend;
int n,m;
int kolkotacaka=0;

int main()
{
	cout<<"unesi broj redova:";
	cin>>n;
	cout<<"unesi broj kolona:";
	cin>>m;
	cout<<"unesi koji broj primera (unesi x ako hoces da se generise schemax.txt i wordsx.txt):";
	cin>>primer;
	cout<<"-----------------"<<'\n'<<"jedno od mogucih resenja ukrstenice:"<<'\n';
	string scheme="schema"+primer+".txt";
	char* schemechars = new char[scheme.length() + 1];
    strcpy(schemechars, scheme.c_str());
    string words="words"+primer+".txt";
	char* wordschars = new char[words.length() + 1];
    strcpy(wordschars, words.c_str());
	ofstream ofs(schemechars);
	ofstream ofw(wordschars);
	srand(time(0));
	kolkotacaka=0;
	for(int i=0;i<105;i++) kolkic[i]=0;
	for (int i=0;i<n;i++)
	{
		vector<char> tmpc;
		kolkotacaka=0;
		for(int j=0;j<m;j++)
		{
			int a;
			if(kolkotacaka>m/MAXDOTSINROW)
			{
				a=0;
				kolkotacaka=m/(MAXDOTSINROW+2);
			}
			else
			{
				a=rand()%2;
				kolkotacaka+=a;	
			}
			if(j!=m-1)
			{
				ofs<<a<<", ";
			}
			else
			{
				ofs<<a;
			}
			if(a==0)
			{
				tmpc.push_back('a'+(rand()%26));
			}
			else
			{
				tmpc.push_back('.');
			}
		}
		ofs<<'\n';
		charsovi.push_back(tmpc);
	}
	string curr;
	for (int i=0;i<n;i++)
	{
		curr="";
		for(int j=0;j<m;j++)
		{
			if(charsovi[i][j]=='.')
			{
				if(curr.length()>0)
				{
					if(strings.count(curr)==0)
					{
						reci.push_back(curr);
						reciend.push_back(curr);
						strings.insert(curr);
						kolkic[curr.length()]++;
					}
				}
				curr="";
			}
			else
			{
				curr+=charsovi[i][j];
			}
			cout<<charsovi[i][j]<<' ';
		}
		if(curr.length()>0)
		{
			if(strings.count(curr)==0)
			{
				reci.push_back(curr);
				reciend.push_back(curr);
				strings.insert(curr);
				kolkic[curr.length()]++;
			}
		}
		cout<<'\n';
	}
	for (int i=0;i<m;i++)
	{
		curr="";
		for(int j=0;j<n;j++)
		{
			if(charsovi[j][i]=='.')
			{
				if(curr.length()>0)
				{
					if(strings.count(curr)==0)
					{
						reci.push_back(curr);
						reciend.push_back(curr);
						strings.insert(curr);
						kolkic[curr.length()]++;
					}
				}
				curr="";
			}
			else
			{
				curr+=charsovi[j][i];
			}
		}
		if(curr.length()>0)
		{
			if(strings.count(curr)==0)
			{
				reci.push_back(curr);
				reciend.push_back(curr);
				strings.insert(curr);
				kolkic[curr.length()]++;
			}
		}
	}
	
	random_shuffle ( reci.begin(), reci.end() ); //ovde shufflujemo da bi se naredna pravila primenjivala na radnom reci
	
	int kolkorandova=reci.size()/MAXCHANGESBIGGER; //maksimalno desetinu (default) od svih reci hocemo da promenimo zbog performansa za vece seme
	if ((n*m)<LIMITFORBIGGERSMALLER) kolkorandova=reci.size()/MAXCHANGESSMALLER; //za manje matrice menjamo veci procenat

	//idemo sa pocetka i kraja i za svaku rec sa 50% verovatnocom gledamo da li cemo da je menjamo
	//recima sa kraja menjamo dva slova a sa pocetka jedno i ubacujemo ako je vec nemamo
	//ponavljamo proces dok ne ubacimo iako je verovatnoca da ce se 2+ iteracije desiti mala
	//
	for(int i=0;i<reci.size();i++)
	{
		if(kolkorandova>0)
		{
			if(i%2==0)
			{
					int x=rand()%2;
					if(x==1)
					{
						while(true)
						{
							int index=rand()%reci[i].length();
							int dodao=0;
							while(true)
							{
								char slovce='a'+rand()%26;
								string temp=reci[i];
								temp[index]=slovce;
								if(strings.count(temp)==0)
								{
									dodao=1;
									strings.insert(temp);
									kolkorandova--;
									reciend.push_back(temp);
									kolkic[temp.length()]++;
									break;
								}
								else if (reci[i].length()<=2)
								{
									if(kolkic[temp.length()]>=pow(26,reci[i].length()))
									{
										dodao=1;
										break;
									}
								}
							}
							if(dodao==1) break;
						}
					}
			}
			else
			{
				int x=rand()%2;
				if(x==1)
				{
					while(true)
					{
						int index1=rand()%reci[reci.size()-i].length();
						int index2=index1;
						if(reci[reci.size()-i].length()>1) while (index2==index1)
						{
							index2=rand()%reci[reci.size()-i].length();
						}
						int dodao=0;
						while(true)
						{
							char slovce1='a'+rand()%26;
							char slovce2='a'+rand()%26;
							string temp=reci[reci.size()-i];
							temp[index1]=slovce1;
							if(reci[reci.size()-i].length()>1) temp[index2]=slovce2;
							if(strings.count(temp)==0)
							{
								strings.insert(temp);
								dodao=1;
								reciend.push_back(temp);
								kolkorandova--;
								kolkic[temp.length()]++;
								break;
							}
							else if (reci[i].length()<=2)
							{
								if(kolkic[temp.length()]>=pow(26,reci[i].length())) //ako smo vec ubacili sve reci odredjene velicine; proveravamo do 2 jer necemo
								{													//imati vise od 1000 reci
									dodao=1;
									break;
								}
							}
						}
						if(dodao==1) break;
					}
				}
			}
		}	
	}
	random_shuffle ( reciend.begin(), reciend.end() );
	for(int i=0;i<reciend.size();i++)
	{
		if (i!=reciend.size()-1) ofw<<reciend[i]<<'\n';
		else ofw<<reciend[i];
	}
	cout<<"pogledaj folder iz kog si pokrenuola exe"<<'\n';
	ofw.close(); 
	ofs.close();	
}
