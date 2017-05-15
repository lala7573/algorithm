#include <iostream>
#include <math.H>

#define PI 3.14159265

using namespace std;

int T, P, X, Y;

//x^2 + y^2 == 2500
bool isBlack(int p, int y, int x) {
	//원 안에 있는지 체크
	if (p == 0) {
		return false;
	}

	if(x*x + y*y > 2500) {
		//white
		return false;
	}

	// 각도를 구한다
	double arc = (double)p/ 50;
	double tan_arc = tan(arc * PI);

	// printf("%fㅠ\t%f\t%d\t%d\t%f\n", arc, tan_arc, x, y, tan_arc*x);
	// printf("%f %d\n", tan_arc * x, y);
	if (p < 50){
		if (y < 0) {
			// printf("5");
			return false;
		}

		if(p <= 25) {
			if (tan_arc*x > y) {
				// printf("1");
				return true;
			} else {
				// printf("2");
				return false;
			}
		} else {
			if (tan_arc*x < y) {
				// printf("3");
				return true;
			} else {
				// printf("4");
				return false;
			}
		}
	} else if (50 <= p) {
		if (y >= 0) {
			// printf("5");
			return true;
		}

		if(p <= 75) {
			if (tan_arc*x < y) {
				// printf("6");
				return true;
			} else {
				// printf("7");
				return false;
			}
		} else {
			if (tan_arc*x > y) {
				// printf("8");
				return true;
			} else {
				// printf("9");
				return false;
			}
		}
	}
	return false;
}
int main() {
	scanf("%d\n", &T);

	for(int i = 0 ;i < T ; i++) {
		scanf("%d %d %d\n", &P, &X, &Y);
		printf("Case #%d: %s\n", i+1, (isBlack(P, X-50, Y-50)? "black": "white"));
	}


	return 0;
}
