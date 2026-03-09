from hypothesis import strategies as st


n_spots = st.integers(min_value=10, max_value=500)
n_genes = st.integers(min_value=5, max_value=200)
exp_value = st.integers()


def generate_random_spatial_data() -> None:  # for property tests
    pass


def create_test_data() -> None:  # for unit tests
    pass
