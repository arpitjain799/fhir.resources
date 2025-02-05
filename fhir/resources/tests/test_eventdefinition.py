# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/EventDefinition
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import eventdefinition


def impl_eventdefinition_1(inst):
    assert inst.id == "example"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.purpose == "Monitor all admissions to Emergency"
    assert inst.status == "draft"
    assert inst.text.status == "generated"
    assert inst.trigger[0].condition.description == (
        "Encounter Location = emergency (active/completed encounters,"
        " current or previous)"
    )
    assert inst.trigger[0].condition.expression == (
        "(%current | %previous).location.where(location = "
        "'Location/emergency' and status in {'active', "
        "'completed'}).exists()"
    )
    assert inst.trigger[0].condition.language == "text/fhirpath"
    assert inst.trigger[0].data[0].type == "Encounter"
    assert inst.trigger[0].name == "monitor-emergency-admissions"
    assert inst.trigger[0].type == "named-event"


def test_eventdefinition_1(base_settings):
    """No. 1 tests collection for EventDefinition.
    Test File: eventdefinition-example.json
    """
    filename = base_settings["unittest_data_dir"] / "eventdefinition-example.json"
    inst = eventdefinition.EventDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "EventDefinition" == inst.resource_type

    impl_eventdefinition_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "EventDefinition" == data["resourceType"]

    inst2 = eventdefinition.EventDefinition(**data)
    impl_eventdefinition_1(inst2)
