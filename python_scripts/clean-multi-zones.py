# clean-multi-zones.py
input_boolean = data.get("input_boolean", ['input_boolean.bano','input_boolean.cocina', 'input_boolean.oficina', 'input_boolean.salon'])
entity_id = data.get("entity_id", 'vacuum.robot_aspirador')
zone_map = data.get("zone_map", [10, 11, 13, 16])
params = [0, 1]
aux = []

i=0
count = 0
while i < len(input_boolean):
    state = hass.states.get(input_boolean[i]).state
    if state == "on":
        aux.append(zone_map[i])
        count = count+1
    i=i+1

params.append(count)
params.extend(aux)

#service_data = {"title": "Titulo", "message": ''.join(str(params))}
#hass.services.call("notify", "persistent_notification", service_data, False)

# Inciciar limpieza
service_data = {"entity_id": entity_id, "command": "set_mode_withroom", "params": params}
hass.services.call("vacuum", "send_command", service_data, False)