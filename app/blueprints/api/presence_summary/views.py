from flask import Blueprint, jsonify

# from .models import PresenceLogSummary
# from blueprints.api.access_ponit.models import AssessPoint

blueprint = Blueprint('api_presence_summary_blueprint', __name__,)



@blueprint.route('/',methods=['GET'])
def presence_summary():
    # access_points = current_session.query(AssessPoint).all()
    # access_point_dict = {}
    # for ap in access_points:
    #     if ap.zone_id == None:
    #         continue
    #     if ap.zone_id in access_point_dict:
    #         access_point_dict[ap.zone_id].append(ap.id)
    #     else:
    #         access_point_dict.update({ap.zone_id:[ap.id]})
    #
    # now = datetime.datetime.utcnow() - datetime.timedelta(minutes=2)
    # before_5_min = now  - datetime.timedelta(minutes=5)
    # before_15_min = now  - datetime.timedelta(minutes=15)
    # before_60_min = now  - datetime.timedelta(minutes=60)
    # before_120_min = now  - datetime.timedelta(minutes=120)
    # before_480_min = now  - datetime.timedelta(minutes=480)
    # before_1_day = now  - datetime.timedelta(days=60)
    # data = {}
    #
    # deleted_rows = current_session.query(PresenceLogSummary).filter(or_(PresenceLogSummary.last_seen <= before_120_min.strftime("%Y-%m-%d %H:%M:%S"),
    #                                                                     PresenceLogSummary.first_seen <= before_480_min.strftime("%Y-%m-%d %H:%M:%S"))).delete(synchronize_session=False)
    # # import pdb;pdb.set_trace()
    # print 'Rows Deleted: '+str(deleted_rows)
    # current_session.commit()
    #
    #
    #
    # tsa_in_5_min_time_query = current_session.query(
    #                                     PresenceLogSummary.mac.label('mac'),
    #                                     (PresenceLogSummary.last_seen - PresenceLogSummary.first_seen).label('duration')
    #                                      )\
    #                                                     .filter(and_(PresenceLogSummary.passed_post_tsa==True,
    #                                                                  ~PresenceLogSummary.first_access_point_id.in_(access_point_dict[1]),
    #                                                                  PresenceLogSummary.last_access_point_id.in_(access_point_dict[4]),
    #                                                                  PresenceLogSummary.last_seen >= before_5_min.strftime("%Y-%m-%d %H:%M:%S"),
    #                                                                  PresenceLogSummary.last_seen <= now.strftime("%Y-%m-%d %H:%M:%S")
    #                                                                  ))
    #
    # tsa_in_5_min_time_data = []
    # num_od_devices_on_transit_period_in_5_min = []
    # for delta in tsa_in_5_min_time_query.all():
    #     seconds = delta.duration.total_seconds()
    #     if seconds >120:
    #         tsa_in_5_min_time_data.append(seconds%3600/60)
    #
    #
    #
    #
    #
    #
    #
    # tsa_in_15_min_time_query = current_session.query(PresenceLogSummary.mac.label('mac'),
    #                                                  (PresenceLogSummary.last_seen - PresenceLogSummary.first_seen).label('duration'))\
    #                                                     .filter(and_(
    #                                                                  PresenceLogSummary.passed_post_tsa==True,
    #                                                                 ~PresenceLogSummary.first_access_point_id.in_(access_point_dict[1]),
    #                                                                  PresenceLogSummary.last_access_point_id.in_(access_point_dict[4]),
    #                                                                  PresenceLogSummary.last_seen >= before_15_min.strftime("%Y-%m-%d %H:%M:%S"),
    #                                                                  PresenceLogSummary.last_seen <= now.strftime("%Y-%m-%d %H:%M:%S")
    #                                                                  ))
    #
    # tsa_in_15_min_time_data = []
    # for delta in tsa_in_15_min_time_query.all():
    #     seconds = delta.duration.total_seconds()
    #     if seconds >120:
    #         tsa_in_15_min_time_data.append(seconds%3600/60)
    #
    #
    # tsa_in_60_min_time_query = current_session.query(PresenceLogSummary.mac.label('mac'),
    #                                                  (PresenceLogSummary.last_seen - PresenceLogSummary.first_seen).label('duration'))\
    #                                                     .filter(and_(PresenceLogSummary.passed_post_tsa==True,
    #                                                                  ~PresenceLogSummary.first_access_point_id.in_(access_point_dict[1]),
    #                                                                  PresenceLogSummary.last_access_point_id.in_(access_point_dict[4]),
    #                                                                  PresenceLogSummary.last_seen >= before_60_min.strftime("%Y-%m-%d %H:%M:%S"),
    #                                                                  PresenceLogSummary.last_seen <= now.strftime("%Y-%m-%d %H:%M:%S")
    #                                                                  ))
    #
    # tsa_in_60_min_time_data = []
    # for delta in tsa_in_60_min_time_query.all():
    #     seconds = delta.duration.total_seconds()
    #     if seconds >120:
    #         tsa_in_60_min_time_data.append(seconds%3600/60)
    #
    #
    #
    #
    # sl_in_5_min_time_query = current_session.query(PresenceLogSummary.mac.label('mac'),
    #                                                (PresenceLogSummary.last_seen - PresenceLogSummary.first_seen).label('duration'))\
    #                                                     .filter(and_(
    #                                                                  PresenceLogSummary.passed_post_tsa==True,
    #                                                                  PresenceLogSummary.passed_security_line==True,
    #                                                                 ~PresenceLogSummary.first_access_point_id.in_(access_point_dict[1]),
    #                                                                  PresenceLogSummary.last_access_point_id.in_(access_point_dict[4]),
    #                                                                  PresenceLogSummary.last_seen >= before_5_min.strftime("%Y-%m-%d %H:%M:%S"),
    #                                                                  PresenceLogSummary.last_seen <= now.strftime("%Y-%m-%d %H:%M:%S")
    #                                                                  ))
    #
    #
    # sl_in_5_min_time_data = []
    # for delta in sl_in_5_min_time_query.all():
    #     seconds = delta.duration.total_seconds()
    #     if seconds >120:
    #         sl_in_5_min_time_data.append(seconds%3600/60)
    #
    #
    #
    # sl_in_15_min_time_query = current_session.query(PresenceLogSummary.mac.label('mac'),
    #                                                 (PresenceLogSummary.last_seen - PresenceLogSummary.first_seen).label('duration'))\
    #                                                     .filter(and_(PresenceLogSummary.passed_post_tsa==True,
    #                                                                  PresenceLogSummary.passed_security_line==True,
    #                                                                  ~PresenceLogSummary.first_access_point_id.in_(access_point_dict[1]),
    #                                                                  PresenceLogSummary.last_access_point_id.in_(access_point_dict[4]),
    #                                                                  PresenceLogSummary.last_seen >= before_15_min.strftime("%Y-%m-%d %H:%M:%S"),
    #                                                                  PresenceLogSummary.last_seen <= now.strftime("%Y-%m-%d %H:%M:%S")
    #                                                                  ))
    #
    #
    #
    # sl_in_15_min_time_data = []
    # for delta in sl_in_15_min_time_query.all():
    #     seconds = delta.duration.total_seconds()
    #     if seconds >120:
    #         sl_in_15_min_time_data.append(seconds%3600/60)
    #
    #
    #
    # sl_in_60_min_time_query = current_session.query(PresenceLogSummary.mac.label('mac'),
    #                                                 (PresenceLogSummary.last_seen - PresenceLogSummary.first_seen).label('duration'))\
    #                                                     .filter(and_(
    #                                                                  PresenceLogSummary.passed_post_tsa==True,
    #                                                                  PresenceLogSummary.passed_security_line==True,
    #                                                                 ~PresenceLogSummary.first_access_point_id.in_(access_point_dict[1]),
    #                                                                  PresenceLogSummary.last_access_point_id.in_(access_point_dict[4]),
    #                                                                  PresenceLogSummary.last_seen >= before_60_min.strftime("%Y-%m-%d %H:%M:%S"),
    #                                                                  PresenceLogSummary.last_seen <= now.strftime("%Y-%m-%d %H:%M:%S")
    #                                                                  ))
    #
    #
    #
    # sl_in_60_min_time_data = []
    # for delta in sl_in_60_min_time_query.all():
    #     seconds = delta.duration.total_seconds()
    #     if seconds >120:
    #         sl_in_60_min_time_data.append(seconds%3600/60)
    #
    #
    #
    #
    #
    # data.update({'transit_period':{
    #     'in_5_min':{
    #         'devices':len(set(tsa_in_5_min_time_data)),
    #         'mean': int(np.mean(sorted(tsa_in_5_min_time_data))) if tsa_in_5_min_time_data else 0,
    #         'median': int(np.median(sorted(tsa_in_5_min_time_data))) if tsa_in_5_min_time_data else 0,
    #         'percentile': int(np.percentile(sorted(tsa_in_5_min_time_data),95)) if tsa_in_5_min_time_data else 0,
    #     },
    #     'in_15_min':{
    #         'devices':len(set(tsa_in_15_min_time_data)),
    #         'mean': int(np.mean(sorted(tsa_in_15_min_time_data))) if tsa_in_15_min_time_data else 0,
    #         'median': int(np.median(sorted(tsa_in_15_min_time_data))) if tsa_in_15_min_time_data else 0,
    #         'percentile': int(np.percentile(sorted(tsa_in_15_min_time_data),95)) if tsa_in_15_min_time_data else 0,
    #     },
    #     'in_60_min':{
    #         'devices':len(set(tsa_in_60_min_time_data)),
    #         'mean': int(np.mean(sorted(tsa_in_60_min_time_data))) if tsa_in_60_min_time_data else 0,
    #         'median': int(np.median(sorted(tsa_in_60_min_time_data))) if tsa_in_60_min_time_data else 0,
    #         'percentile': int(np.percentile(sorted(tsa_in_60_min_time_data),95)) if tsa_in_60_min_time_data else 0,
    #     }
    # },'security_period':{
    #     'in_5_min':{
    #         'devices':len(set(sl_in_5_min_time_data)),
    #         'mean': int(np.mean(sorted(sl_in_5_min_time_data))) if sl_in_5_min_time_data else 0,
    #         'median': int(np.median(sorted(sl_in_5_min_time_data))) if sl_in_5_min_time_data else 0,
    #         'percentile': int(np.percentile(sorted(sl_in_5_min_time_data),95)) if sl_in_5_min_time_data else 0,
    #     },
    #     'in_15_min':{
    #         'devices':len(set(sl_in_15_min_time_data)),
    #         'mean': int(np.mean(sorted(sl_in_15_min_time_data))) if sl_in_15_min_time_data else 0,
    #         'median': int(np.median(sorted(sl_in_15_min_time_data))) if sl_in_15_min_time_data else 0,
    #         'percentile': int(np.percentile(sorted(sl_in_15_min_time_data),95)) if sl_in_15_min_time_data else 0,
    #     },
    #     'in_60_min':{
    #         'devices':len(set(sl_in_60_min_time_data)),
    #         'mean': int(np.mean(sorted(sl_in_60_min_time_data))) if sl_in_60_min_time_data else 0,
    #         'median': int(np.median(sorted(sl_in_60_min_time_data))) if sl_in_60_min_time_data else 0,
    #         'percentile': int(np.percentile(sorted(sl_in_60_min_time_data),95)) if sl_in_60_min_time_data else 0,
    #     }
    # }
    # })
    #
    #

    # response = current_app.response_class(
    #     response=json.dumps({'message':'Success--------'}),
    #     status=200,
    #     mimetype='application/json'
    # )
    # return response
    return jsonify({'message':'success'})