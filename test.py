version = 2
padding = 0
extension = 0
cc = 0
marker = 0
pt = 26 # MJPEG type
seqnum = frameNbr
ssrc = 0 
header[0] = (header[0] | version << 6) & 0xC0 # 2 bits
header[0] = (header[0] | padding << 5) # 1 bit
header[0] = (header[0] | extension << 4) # 1 bit
header[0] = (header[0] | (cc & 0x0F)) # 4 bits
header[1] = (header[1] | marker << 7) # 1 bit
header[1] = (header[1] | (pt & 0x7f)) # 7 bits
header[2] = (seqnum & 0xFF00) >> 8 # 16 bits total, this is first 8
header[3] = (seqnum & 0xFF) # second 8
header[4] = (timestamp >> 24) # 32 bit timestamp
header[5] = (timestamp >> 16) & 0xFF
header[6] = (timestamp >> 8) & 0xFF
header[7] = (timestamp & 0xFF)
header[8] = (ssrc >> 24);# 32 bit ssrc
header[9] = (ssrc >> 16) & 0xFF
header[10] = (ssrc >> 8) & 0xFF
header[11] = ssrc & 0xFF