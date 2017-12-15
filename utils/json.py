import json


def model_to_json(objects, fields_list):
    """
        将orm obj 转换成json对象
    :param objects: User.objects.all()
    :param fields_list: ['name', 'group', 'gender', 'birthday', ...]
    :return: (json)
    """
    json_rv = []  # 输出各field的值到字典
    for obj in objects:
        fields = fields_list
        d = {}
        for f in fields:
            if f == 'working_position':
                print('1')
                pass
            s = 'get_{}_display'.format(f)
            if hasattr(obj, s):
                # 如 'gender'则返回'男'而非'male'
                d[f] = getattr(obj, s)()
            else:
                d[f] = getattr(obj, f)
            # None则返回空串
            d[f] = str(d[f]) if d[f] else ''
        json_rv.append(d)

    return json.dumps(json_rv)
