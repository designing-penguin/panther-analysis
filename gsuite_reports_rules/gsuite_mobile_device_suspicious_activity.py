from panther_base_helpers import gsuite_details_lookup as details_lookup


def rule(event):
    if event['id'].get('applicationName') != 'mobile':
        return False

    return bool(
        details_lookup('suspicious_activity', ['SUSPICIOUS_ACTIVITY_EVENT'],
                       event))


def title(event):
    return 'User [{}]\'s device was compromised'.format(
        event.get('actor', {}).get('email'))
