

def collect_checkboxes(post, check="on"):
    """
    Returns a list of all args whos value == bool
    """
    l = []
    for a in post:
        if post[a] == check:
            l.append(a)
    return l


def add_results_to_context(context, results):
    """
    Returns context appended with all search results
    """
    for a in results:
        # if context[a]:
        #     next
        if results[a]:
            context[a] = results[a]["items"]
    return context
    