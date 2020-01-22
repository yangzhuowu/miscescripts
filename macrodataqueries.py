# -*- coding: utf-8 -*-
sqlquery = ''' SELECT
                    dd.datekey,
                    dd.value,
                    rr.country_code,
                    cc.variable_name,
                    mm.series_id,
                    mm.region_id,
                    mm.variable_id,
                    mm.provider_id,
                    mm.frequency,
                    mm.base_year,
                    mm.currency,
                    mm.unit,
                    mm.multiplier,
                    mm.series_nature,
                    mm.is_seasonally_adjusted,
                    mm.is_real,
                    pp.is_main_source
            FROM
                    DATA_SERIES dd,
                    METADATA mm,
                    REGIONS rr,
                    CONCEPTS cc,
                    DATA_PROVIDERS pp
            WHERE   dd.id = mm.series_id
            AND     mm.region_id = rr.id
            AND     mm.variable_id = cc.id
            AND     mm.provider_id = pp.id
            AND     cc.varibale_name = "%s"
            '''

