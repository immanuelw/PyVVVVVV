from __future__ import print_function
import json

rect_list = {0:
				{1:
					((0, 0, 52, 92),
					(0, 92, 176, 40),
					(176, 106, 40, 26),
					(216, 106, 102, 26),
					(216, 92, 64, 16),
					(40, 133, 48, 15),
					(128, 133, 48, 15),
					(216, 133, 48, 15),
					(92, 10, 228, 20),
					(92, 21, 28, 15),
					(160, 21, 172, 15),
					(272, 21, 148, 15),
					(0, 219, 320, 21),
					(0, 204, 44, 15),
					(84, 204, 48, 15),
					(172, 204, 48, 15),
					(260, 1204, 60, 15)),		

				2:
					((0, 0, 52, 240),
					(52, 100, 80, 40),
					(92, 0, 40, 52),
					(132, 0, 136, 20),
					(268, 0, 52, 52),
					(92, 188, 40, 32),
					(132, 218, 136, 22),
					(268, 188, 52, 52)),		

				3:
					((0, 0, 52, 240),
					(52, 92, 130, 56),
					(202, 92, 58, 56),
					(182, 116, 40, 8),
					(92, 16, 40, 36),
					(152, 16, 72, 36),
					(284, 16, 16, 36),
					(300, 0, 20, 240),
					(92, 0, 228, 16),
					(92, 188, 40, 40),
					(152, 188, 148, 52),
					(92, 228, 64, 12)),		

				4:
					((0, 0, 52, 240),
					(92, 0, 228, 52),
					(180, 52, 48, 12),
					(52, 108, 68, 8),
					(160, 92, 11, 8),
					(52, 116, 200, 32),
					(252, 92, 68, 72),
					(92, 204, 40, 12),
					(236, 204, 84, 36),
					(92, 216, 144, 24)),		

				5:
					((0, 0, 320, 36),
					(300, 36, 20, 96),
					(0, 36, 100, 112),
					(100, 108, 80, 40),
					(0, 148, 52, 82),
					(92, 188, 228, 52),
					(204, 76, 56, 112),
					(147, 58, 26, 17))
				},

			1:
				{1:
					((0, 0, 320, 36),
					(0, 204, 320, 240),
					(0, 107, 320, 26),
					(150, 133, 20, 15),
					(100, 92, 220, 15)),		

				2:
					((0, 0, 320, 36),
					(0, 36, 68, 16),
					(148, 36, 24, 8),
					(208, 36, 24, 8),
					(148, 56, 24, 24),
					(208, 56, 24, 24),
					(0, 188, 124, 36),
					(140, 188, 44, 36),
					(200, 188, 40, 36),
					(256, 188, 28, 36),
					(284, 36, 36, 188),
					(0, 224, 320, 16)),
				
				3:
					((0, 0, 11, 240),
					(11, 0, 309, 12),
					(187, 12, 133, 88),
					(12, 188, 308, 52)),

				4:
					((0, 0, 320, 52),
					(284, 52, 36, 152),
					(0, 204, 284, 36),
					(0, 92, 244, 72)),		

				5:
					((0, 0, 20, 132),
					(20, 0, 300, 36),
					(108, 36, 212, 16),
					(108, 52, 152, 32),
					(220, 84, 40, 96),
					(284, 108, 36, 132),
					(196, 220, 88, 20),
					(0, 188, 44, 52),
					(44, 76, 40, 164),
					(84, 172, 112, 68))
				},
				
			2:
				{1:
					((0, 0, 132, 36),
					(188, 0, 132, 52),
					(188, 52, 40, 40),
					(0, 92, 228, 40),
					(0, 204, 52, 36),
					(92, 132, 136, 108),
					(284, 92, 36, 148)),		

				2:
					((0, 0, 132, 240),
					(132, 0, 188, 36),
					(188, 140, 132, 100)),		

				3:
					((0, 0, 320, 100),
					(0, 188, 110, 52),
					(210, 188, 110, 52),
					(110, 206, 100, 34)),		

				4:
					((0, 0, 196, 84),
					(0, 84, 68, 14),
					(0, 100, 12, 72),
					(0, 172, 12, 68),
					(12, 164, 40, 13),
					(10, 160, 160, 12),
					(180, 164, 40, 8),
					(220, 0, 320, 240),
					(124, 84, 40, 8)),		

				5:
					((0, 0, 100, 52),
					(100, 0, 90, 26),
					(190, 26, 126, 26),
					(60, 52, 40, 92),
					(0, 108, 32, 64),
					(0, 172, 132, 32),
					(0, 204, 192, 36),
					(220, 92, 40, 148),
					(260, 124, 60, 116))
				},

			3:
				{0:
					((0, 0, 116, 36),
					(76, 36, 40, 128),
					(204, 0, 116, 36),
					(294, 36, 40, 128),
					(92, 164, 136, 16)),

				1:
					((0, 0, 140, 36),
					(0, 36, 56, 16),
					(180, 0, 140, 36),
					(264, 36, 56, 16),
					(0, 76, 82, 164),
					(82, 90, 34, 150),
					(204, 90, 34, 150),
					(238, 76, 82, 154),
					(140, 128, 40, 24)),		

				2:
					((0, 0, 320, 36),
					(0, 140, 140, 100),
					(180, 140, 140, 100)),		

				3:
					((0, 188, 320, 52),
					(284, 0, 56, 188),
					(0, 0, 36, 100),
					(36, 60, 112, 50),
					(60, 96, 88, 36)),
				
				4:
					((0, 0, 36, 240),
					(284, 0, 36, 240)),		

				5:
					((284, 0, 36, 240),
					(0, 0, 115, 52),
					(115, 0, 34, 8),
					(149, 0, 135, 52),
					(0, 124, 40, 116),
					(40, 168, 204, 28),
					(70, 124, 120, 44),
					(220, 124, 24, 44))
				},

			4:
				{1:
					((0, 204, 320, 36),
					(0, 108, 36, 96),
					(0, 0, 132, 68),
					(60, 68, 72, 96),
					(132, 92, 64, 72),
					(196, 128, 56, 36),
					(252, 92, 68, 72),
					(188, 0, 132, 26),
					(202, 36, 42, 8)),		

				2:
					((0, 0, 180, 36),
					(180, 0, 40, 21),
					(220, 0, 100, 132),
					(188, 132, 132, 108),
					(0, 140, 92, 36),
					(92, 76, 40, 164),
					(132, 132, 32, 40))
				},

			5:
				{1:
					((0, 0, 320, 36),
					(28, 36, 40, 16),
					(108, 36, 104, 16),
					(252, 36, 40, 16),
					(0, 204, 320, 36),
					(0, 92, 84, 72),
					(84, 92, 24, 36),
					(108, 92, 24, 72),
					(132, 124, 56, 40),
					(188, 92, 22, 36),
					(210, 92, 26, 36),
					(236, 92, 84, 72))
				},

			6:
				{1:
					((0, 0, 320, 36),
					(284, 36, 36, 136),
					(156, 172, 164, 68),
					(0, 204, 100, 36),
					(0, 92, 36, 16),
					(0, 108, 68, 16),
					(0, 124, 100, 16),
					(0, 140, 132, 16),
					(0, 156, 156, 24),
					(156, 168, 4, 80))
				}
			}

if __name__ == '__main__':
	level_array = tuple((x,y) for x, val in rect_list.items() for y, value in val.items())
	rects = {x_co: {y_co: rect_list[x_co][y_co] if (x_co, y_co) in level_array else ((0, 0, 0, 0),) for y_co in range(7)} for x_co in range(7)}
	print(level_array)
	#print(rects)

	backup_path = './storage/rects.json'
	with open(backup_path, 'w') as bkup:
		json.dump(rects, bkup, sort_keys=True, indent=4)
