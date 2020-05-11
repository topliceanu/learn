# -*- coding: utf-8 -*-

# We have a stream of metrics and tags that we receive from our customers and we want to build a
# page to summarize the tags they send.
#
# We want to add a dropdown menu to our page to allow users to filter the page content. The menu
# initially lists all possible tags, but as the user enters one or more tags the list of available
# options is limited to those tags that are related to the entered tags.
#
# Write the function that powers this dropdown menu. Specifically, given a stream of strings in
# the form '<metric>|<value>|<tags>' (e.g. 'system.load.1|1|host:a,role:web,region:us-east-1a')
# write a function that takes this stream and a set of tags as parameters and returns all the tags that are
# associated with them. Order does not matter.


def build_indices(stream):
    """ Parses the stream of logs and indexes it.
    Args:
        stream, list of string, format <metric_name>|<value>|<coma_separated_tags>
    Returns:
        pair of hashes,
            first hash has the format {tag -> set([line_indices])}
            second hash has the format {line_index -> set([tags])}
    """
    tag_index = {} # tag -> [line_ids]
    line_index = {} # line_id -> [tag]
    for i in range(len(stream)):
        line = stream[i]
        segments = line.split("|")
        tags = segments[2].split(",")
        line_index[i] = set(tags)
        for tag in tags:
            if tag not in tag_index:
                tag_index[tag] = set([])
            tag_index[tag].add(i)
    return tag_index, line_index

def intersect(index, keys):
    """ Utility method to compute the intersection of all the sets in index
    that correspond to the given keys keys.
    Args:
        index, hash for format {key -> set()}
        keys, list of strings
    Returns:
        set, the intersection of all the sets in index that correspond to keys.
            If there is at least on key that does not exist in index, this
            method will return an empty set.
    """
    if len(keys) == 0:
        return set([])
    if keys[0] not in index:
        return set([])
    output = index[keys[0]]
    for i in range(1, len(keys)):
        key = keys[i]
        if key not in index:
            return set([])
        output = output.intersection(index[key])
    return output

def search(tag_index, line_index, and_tags):
    """ Returns all the tags that are in common lines for all tags in and_tags.
    Args:
        tag_index: hash with format {tag -> set([line_indices])}
        line_index: hash with format {line_index -> set([tags])}
        and_tags: list of tags
    Returns:
        set, of tags
    """
    lines = intersect(tag_index, and_tags)
    if len(lines) == 0:
        return set([])
    output = intersect(line_index, list(lines))
    return output - set(and_tags)

def find_related_tags(stream, tags):
    if len(tags) == 0 or len(stream) == 0:
        return []

    # preprocessing: build the index
    tag_index, line_index = build_indices(stream)

    # return search results
    return list(search(tag_index, line_index, tags))
