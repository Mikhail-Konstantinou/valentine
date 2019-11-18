from itertools import product


def compute_ssim(node_s, node_t, sims, th_accept=0.5):
    s_leaves = list(map(lambda n: n.name.initial_name, node_s.leaves))
    t_leaves = list(map(lambda n: n.name.initial_name, node_t.leaves))

    s_strong_link = set()
    t_strong_link = set()

    for s in s_leaves:
        for t in t_leaves:
            if sims[(s, t)]['wsim'] > th_accept:
                s_strong_link.add(s)
                t_strong_link.add(t)

    return (len(s_strong_link) + len(t_strong_link)) / (len(s_leaves) + len(t_leaves))


def change_structural_similarity(leaves_s, leaves_t, sims, factor):
    all_leaves = product(leaves_s, leaves_t)

    for pair in all_leaves:
        sims[pair]['ssim'] = sims[pair]['ssim'] * factor
