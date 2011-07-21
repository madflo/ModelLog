from hashlib import sha256
import settings
import json

def at_log(log):
    try:
        log['event_id']             #5.1.1. Event ID                        required
        log['event_action_code']    #5.1.2. Event Action Code,              optional
        log['event_date']           #5.1.3. Event Date/Time                 required
        log['event_outcome']        #5.1.4. Event Outcome Indicator         required
        log['user_id']              #5.2.1. User ID                         required
        log['access_point_ip']      #5.3.2. Network Access Point ID         optional
        log['source_id']            #5.4.2. Audit Source ID                 required
        log['instance_id_type']     #5.5.4. Participant Object ID Type Code required
        log['instance_id']          #5.5.6. Participant Object ID           required
    except Exception as e:
        raise e #TODO: I don't know
    log_keys = log.keys()
    log_keys.sort()
    log_hash = sha256(settings.SECRET_KEY)
    for key in log_keys:
        log_hash.update(str(log[key]))
    log['signature'] = log_hash.hexdigest()
    settings.logger.info(json.dumps(log, sort_keys = True))
