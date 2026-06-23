from django import forms
from .models import RecruitmentApplication


class RecruitmentApplicationForm(forms.ModelForm):
    class Meta:
        model = RecruitmentApplication
        fields = [
            'name', 'gender', 'college', 'major', 'grade', 'phone', 'qq', 'wechat', 'email',
            'target_group', 'has_basic', 'skills', 'experience', 'reason', 'available_time',
            'accept_assessment', 'attachment'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': '请输入姓名'}),
            'gender': forms.Select(choices=(('', '请选择'), ('男', '男'), ('女', '女'))),
            'college': forms.TextInput(attrs={'placeholder': '例如：智能制造学院'}),
            'major': forms.TextInput(attrs={'placeholder': '例如：信息管理与信息系统'}),
            'grade': forms.TextInput(attrs={'placeholder': '例如：2025级'}),
            'phone': forms.TextInput(attrs={'placeholder': '用于招新通知'}),
            'qq': forms.TextInput(attrs={'placeholder': '可选'}),
            'wechat': forms.TextInput(attrs={'placeholder': '可选'}),
            'email': forms.EmailInput(attrs={'placeholder': '可选'}),
            'target_group': forms.Select(choices=(
                ('机械结构组', '机械结构组'),
                ('嵌入式电控组', '嵌入式电控组'),
                ('算法视觉组', '算法视觉组'),
                ('导航定位组', '导航定位组'),
                ('运营宣传组', '运营宣传组'),
                ('招商外联组', '招商外联组'),
                ('项目管理组', '项目管理组'),
                ('暂不确定，希望了解后选择', '暂不确定，希望了解后选择'),
            )),
            'has_basic': forms.Select(choices=(('', '请选择'), ('零基础但愿意学', '零基础但愿意学'), ('有课程基础', '有课程基础'), ('有项目/竞赛经验', '有项目/竞赛经验'))),
            'skills': forms.Textarea(attrs={'rows': 4, 'placeholder': '例如 C/C++、Python、SolidWorks、STM32、OpenCV、剪辑、摄影等'}),
            'experience': forms.Textarea(attrs={'rows': 4, 'placeholder': '写写你参与过的项目、比赛、课程设计或个人作品'}),
            'reason': forms.Textarea(attrs={'rows': 5, 'placeholder': '为什么想加入 LionHeart？希望在战队获得什么成长？'}),
            'available_time': forms.TextInput(attrs={'placeholder': '例如：每周 8-12 小时'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'accept_assessment':
                field.widget.attrs.update({'class': 'form-check-input'})
            elif field_name == 'attachment':
                field.widget.attrs.update({'class': 'form-control'})
            else:
                field.widget.attrs.update({'class': 'form-control'})
