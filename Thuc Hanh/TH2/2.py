from shapely.geometry import Polygon


def tinh_dien_tich_che_phu(tam_giac):
    polygons = []
    for tg in tam_giac:
        polygon = Polygon(tg)
        polygons.append(polygon)

    polygon_hop_nhat = polygons[0]
    for polygon in polygons[1:]:
        polygon_hop_nhat = polygon_hop_nhat.union(polygon)

    return polygon_hop_nhat.area


def nhap_du_lieu(n):
    tam_giac = []
    for i in range(n):
        toa_do = list(map(float, input().split()))
        tam_giac.append(
            [(toa_do[0], toa_do[1]), (toa_do[2], toa_do[3]), (toa_do[4], toa_do[5])]
        )
    return tam_giac


n = int(input())
tam_giac = nhap_du_lieu(n)
dien_tich = tinh_dien_tich_che_phu(tam_giac)

print(f"{dien_tich:.6f}")
