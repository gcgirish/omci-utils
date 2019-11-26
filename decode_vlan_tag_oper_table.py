# Copyright 2019 Girish G C
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

OUTER_PRIORITY_BITS = 4
OUTER_VID_BITS = 13
OUTER_TPID_BITS = 3
OUTER_PADDING_BITS = 12
INNER_PRIORITY_BITS = 4
INNER_VID_BITS = 13
INNER_TPID_BITS = 3
INNER_PAD_BITS = 8
ETHER_TYPE_BITS = 4
TAGS_TO_REMOVE_BITS = 2
PADDING_BITS_1 = 10
TREATEMENT_OUTER_PRIORITY_BITS = 4
TREATMENT_OUTER_VID_BITS = 13
TREATMENT_OUTER_TPID_BITS = 3
PADDING_BITS_2 = 12
TREATMENT_INNER_PRIORITY_BITS = 4
TREATMENT_INNER_VID_BITS = 13
TREATMENT_INNER_TPID_BITS = 3


def print_filter_outer_priority(val):
    print("== Filter outer priority ==")
    if 0 <= val <= 7:
        print("Filter received frames on this outer priority (P bit) value: %d" % val)
    elif val == 8:
        print("Do not filter on outer priority")
    elif val == 14:
        print("This is the default filter when no other two-tag rule applies")
    elif val == 15:
        print("This entry is not a double-tag rule; ignore all other outer tag filter fields")
    else:
        print("reserved: %d" % val)


def print_filter_outer_vid(val):
    print("== Filter outer VID ==")
    if 0 <= val <= 4094:
        print("Filter received frames on this outer VID value: %d" % val)
    elif val == 4096:
        print("Do not filter on the outer VID")
    else:
        print("reserved")


def print_filter_outer_tpid_dei(val):
    print("== Filter outer TPID/DEI == ")
    if val == 0:
        print("Do not filter on outer TPID field")
    elif val == 4:
        print("Outer TPID = 0x8100")
    elif val == 5:
        print("Outer TPID = input TPID attribute value, don't care about DEI bit")
    elif val == 6:
        print("Outer TPID = input TPID, DEI = 0")
    elif val == 7:
        print("Outer TPID = input TPID, DEI = 1")
    else:
        print("INVALID OUTER TPID DEI")


def print_filter_inner_priority(val):
    print("== Filter inner priority ==")
    if 0 <= val <= 7:
        print("Filter received frames on this inner priority value: %d" % val)
    elif val == 8:
        print("Do not filter on inner priority")
    elif val == 14:
        print("This is the default filter when no other one-tag rule applies.")
    elif val == 15:
        print("This entry is a no-tag rule; ignore all other VLAN tag filter fields")
    else:
        print("INVALID filter inner priority value %d" % val)


def print_filter_inner_vid(val):
    print("Filter inner VID")
    if 0 <= val <= 4094:
        print("Filter received frames on this inner VID value: %d" % val)
    elif val == 4096:
        print("Do not filter on the inner VID")
    else:
        print("reserved")


def print_filter_inner_tpid_dei(val):
    print("== Filter inner TPID/DEI == ")
    if val == 0:
        print("Do not filter on inner TPID field")
    elif val == 4:
        print("Inner TPID = 0x8100")
    elif val == 5:
        print("Inner TPID = input TPID attribute value, don't care about DEI bit")
    elif val == 6:
        print("Inner TPID = input TPID, DEI = 0")
    elif val == 7:
        print("Inner TPID = input TPID, DEI = 1")
    else:
        print("INVALID INNER TPID DEI")


def print_filter_ether_type(val):
    print("== Filter Ethertype: ==")
    if val == 0:
        print("Do not filter on Ethertype")
    elif val == 1:
        print("Ethertype = 0x0800 (filter IPoE frames)")
    elif val == 2:
        print("Ethertype = 0x8863 or 0x8864 (filter PPPoE frames)")
    elif val == 3:
        print("Ethertype = 0x0806 (filter ARP frames)")
    elif val == 4:
        print("Ethertype = 0x86DD (filter IPv6 IpoE frames)")
    else:
        print("RESERVED: %d" % val)


def print_filter_treatment_tags_to_remove(val):
    print("== Treatment tags to remove ==")
    if 0 <= val <= 2:
        print("Remove 0, 1 or 2 tags, respectively. If one tag is specified, "
              "then the outer tag is stripped from double-tagged frames: %d" % val)
    else:
        print("Discard the frame. No symmetric downstream operation exists; "
              "i.e., this rule is ignored in the downstream direction")


def print_treatment_outer_priority(val):
    print(" == Treatment outer priority == ")
    if 0 <= val <= 7:
        print("Add an outer tag, and insert this value as the priority in the "
              "outer VLAN tag: %d" % val)
    elif val == 8:
        print("Add an outer tag, and copy the outer priority from the inner "
              "priority of the received frame")
    elif val == 9:
        print("Add an outer tag, and copy the outer priority from the outer "
              "priority of the received frame")
    elif val == 10:
        print("Add an outer tag, and derive P bits from the DSCP field of the "
              "incoming frame according to the DSCP to P-bit mapping attribute")
    elif val == 15:
        print("Do not add an outer tag")
    else:
        print("Reserved: %d" % val)


def print_treatment_outer_vid(val):
    print("== Treatment outer VID ==")
    if 0 <= val <= 4094:
        print("Use this value as the VID in the outer VLAN tag: %d" % val)
    elif val == 4096:
        print("Copy the outer VID from the inner VID of the received frame")
    elif val == 4097:
        print("Copy the outer VID from the outer VID of the received frame.")
    else:
        print("RESERVED: %d" % val)


def print_treatment_outer_tpid_dei(val):
    print("== Treatment outer TPID/DEI ==")
    if val == 0:
        print("Copy TPID (and DEI, if present) from the inner tag of the "
              "received frame")
    elif val == 1:
        print("Copy TPID (and DEI, if present) from the outer tag of the "
              "received frame")
    elif val == 2:
        print("Set TPID = output TPID attribute value, copy DEI bit from "
              "the inner tag of the received frame")
    elif val == 3:
        print("Set TPID = output TPID, copy DEI from the outer tag of the "
              "received frame")
    elif val == 4:
        print("Set TPID = 0x8100")
    elif val == 5:
        print("Reserved")
    elif val == 6:
        print("Set TPID = output TPID, DEI = 0")
    elif val == 7:
        print("Set TPID = output TPID, DEI = 1")


def print_treatment_inner_priority(val):
    print("== Treatment inner priority ==")
    if 0 <= val <= 7:
        print("Add an inner tag, and insert this value as the priority to "
              "insert in the inner VLAN tag: %d" % val)
    elif val == 8:
        print("Add an inner tag, and copy the inner priority from the inner "
              "priority of the received frame")
    elif val == 9:
        print("Add an inner tag, and copy the inner priority from the outer "
              "priority of the received frame")
    elif val == 10:
        print("Add an inner tag, and derive P bits from the DSCP field of "
              "the incoming frame according to the DSCP to P-bit mapping attribute.")
    elif val == 15:
        print("Do not add an inner tag.")
    else:
        print("RESERVED: %d" % val)


def print_treatment_inner_vid(val):
    print("== Treatment inner VID ==")
    if 0 <= val <= 4094:
        print("Use this value as the VID in the innver VLAN tag: %d" % val)
    elif val == 4096:
        print("Copy the innver VID from the inner VID of the received frame")
    elif val == 4097:
        print("Copy the inner VID from the outer VID of the received frame.")
    else:
        print("RESERVED: %d" % val)


def print_treatment_inner_tpid_dei(val):
    print("== Treatment inner TPID/DEI == ")
    if val == 0:
        print("Copy TPID (and DEI, if present) from the inner tag of the "
              "received frame")
    elif val == 1:
        print("Copy TPID (and DEI, if present) from the outer tag of the "
              "received frame")
    elif val == 2:
        print("Set TPID = output TPID attribute value, copy DEI bit from "
              "the inner tag of the received frame")
    elif val == 3:
        print("Set TPID = output TPID, copy DEI from the outer tag of the "
              "received frame")
    elif val == 4:
        print("Set TPID = 0x8100")
    elif val == 5:
        print("Reserved")
    elif val == 6:
        print("Set TPID = output TPID, DEI = 0")
    elif val == 7:
        print("Set TPID = output TPID, DEI = 1")


def decode_vlan_tag_oper_table_data(hex_data):
    print("***************************************************************************************************")
    print("Received frame VLAN tagging operation table: %x" % hex_data)
    print("***************************************************************************************************")
    print("***************************************************************************************************")
    print("Decoding begin")
    print("***************************************************************************************************")
    # remove first two characters '0b' after converting to binary
    binary = bin(hex_data)[2:]

    # Decode -> Filter outer priority
    sub_str = binary[0:OUTER_PRIORITY_BITS]
    print_filter_outer_priority(int(sub_str, 2))
    binary = binary[OUTER_PRIORITY_BITS: len(binary)]

    print("***************************************************************************************************")

    # Decode -> Filter outer VID
    sub_str = binary[0:OUTER_VID_BITS]
    print_filter_outer_vid(int(sub_str, 2))
    binary = binary[OUTER_VID_BITS: len(binary)]

    print("***************************************************************************************************")

    # Decode -> Filter outer TPID/DEI
    sub_str = binary[0:OUTER_TPID_BITS]
    print_filter_outer_tpid_dei(int(sub_str, 2))
    binary = binary[OUTER_TPID_BITS: len(binary)]

    print("***************************************************************************************************")

    # Ignore 12 bits of padding
    binary = binary[OUTER_PADDING_BITS: len(binary)]

    # Decode -> Filter inner priority
    sub_str = binary[0:INNER_PRIORITY_BITS]
    print_filter_inner_priority(int(sub_str, 2))
    binary = binary[INNER_PRIORITY_BITS: len(binary)]

    print("***************************************************************************************************")

    # Decode -> Filter inner VID:
    sub_str = binary[0:INNER_VID_BITS]
    print_filter_inner_vid(int(sub_str, 2))
    binary = binary[INNER_VID_BITS: len(binary)]

    print("***************************************************************************************************")

    # Decode -> Filter inner TPID/DEI:
    sub_str = binary[0:INNER_TPID_BITS]
    print_filter_inner_tpid_dei(int(sub_str, 2))
    binary = binary[INNER_TPID_BITS: len(binary)]

    # Ignore 8 bits of padding
    binary = binary[INNER_PAD_BITS: len(binary)]

    print("***************************************************************************************************")

    # Decode -> Filter Ethertype
    sub_str = binary[0:ETHER_TYPE_BITS]
    print_filter_ether_type(int(sub_str, 2))
    binary = binary[ETHER_TYPE_BITS: len(binary)]

    print("***************************************************************************************************")

    # Decode -> Treatment tags to remove
    sub_str = binary[0:TAGS_TO_REMOVE_BITS]
    print_filter_treatment_tags_to_remove(int(sub_str, 2))
    binary = binary[TAGS_TO_REMOVE_BITS: len(binary)]

    print("***************************************************************************************************")

    # Ignore 10 bits of padding
    binary = binary[PADDING_BITS_1: len(binary)]

    # Decode -> Treatment outer priority
    sub_str = binary[0:TREATEMENT_OUTER_PRIORITY_BITS]
    print_treatment_outer_priority(int(sub_str, 2))
    binary = binary[TREATEMENT_OUTER_PRIORITY_BITS: len(binary)]

    print("***************************************************************************************************")

    # Decode -> Treatment outer VID
    sub_str = binary[0:TREATMENT_OUTER_VID_BITS]
    print_treatment_outer_vid(int(sub_str, 2))
    binary = binary[TREATMENT_OUTER_VID_BITS: len(binary)]

    print("***************************************************************************************************")

    # Decode -> Treatment outer TPID/DEI
    sub_str = binary[0:TREATMENT_OUTER_TPID_BITS]
    print_treatment_outer_tpid_dei(int(sub_str, 2))
    binary = binary[TREATMENT_OUTER_TPID_BITS: len(binary)]

    # Ignore 12 bits of padding
    binary = binary[PADDING_BITS_2: len(binary)]

    print("***************************************************************************************************")

    # Decode -> Treatment inner priority
    sub_str = binary[0:TREATMENT_INNER_PRIORITY_BITS]
    print_treatment_inner_priority(int(sub_str, 2))
    binary = binary[TREATMENT_INNER_PRIORITY_BITS: len(binary)]

    print("***************************************************************************************************")

    # Decode -> Treatment inner VID
    sub_str = binary[0:TREATMENT_INNER_VID_BITS]
    print_treatment_inner_vid(int(sub_str, 2))
    binary = binary[TREATMENT_INNER_VID_BITS: len(binary)]

    print("***************************************************************************************************")

    # Decode -> Treatment inner TPID/DEI
    sub_str = binary[0:TREATMENT_INNER_TPID_BITS]
    print_treatment_inner_tpid_dei(int(sub_str, 2))
    print("***************************************************************************************************")
    binary = binary[TREATMENT_INNER_TPID_BITS: len(binary)]
    if len(binary) != 0:
        print("SOMETHING WRONG: THERE IS LEFT OVER DATA TO BE DECODED!!")


if __name__ == "__main__":
    hex_num = input("input vlan_tag_oper_table_data string->")
    decode_vlan_tag_oper_table_data(int(hex_num, 16))
