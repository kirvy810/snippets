#include <concepts>
#include <tuple>

template <std::integral M, std::integral N>
constexpr auto xgcd(M a, N b) {
    using I = std::common_type_t<M, N>;
    using R = std::tuple<I, I, I>;
    
	if (b == 0)
		return R{a, 1, 0};
	auto [d, s, t] = xgcd(b, a % b);
	return R{d, t, s - a / b * t};
}

int main() {
    return 0;
}
