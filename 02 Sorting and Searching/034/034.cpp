#include <algorithm>
#include <iostream>
#include <set>
#include <vector>

using std::cout;
using std::endl;
using std::vector;

int main() {
	int street_len;
	int light_num;
	std::cin >> street_len >> light_num;
	vector<int> lights(light_num);
	for (int &l : lights) { std::cin >> l; }
	std::set<int> street_pos{0, street_len};
	for (int l : lights) { street_pos.insert(l); }

	vector<int> gaps(light_num);
	int prev = 0;
	int max_gap = 0;
	for (int p : street_pos) {
		max_gap = std::max(max_gap, p - prev);
		prev = p;
	}
	gaps.back() = max_gap;
	for (int i = light_num - 1; i > 0; i--) {
		street_pos.erase(lights[i]);
		auto high_it = street_pos.upper_bound(lights[i]);
		int high = *high_it;
		int low = *(--high_it);
		max_gap = std::max(max_gap, high - low);
		gaps[i - 1] = max_gap;
	}

	for (int i = 0; i < gaps.size() - 1; i++) { cout << gaps[i] << ' '; }
	cout << gaps.back() << endl;
}