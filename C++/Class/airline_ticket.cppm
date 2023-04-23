export module airline_ticket;
#include <string>
using namespace std;

export class AirlineTicket {
	public:
		AirlineTicket();
		~AirlineTicket();

		double calPrice();

		string getName();
		void setName(string name);

		int getMiles();
		void setMine


};