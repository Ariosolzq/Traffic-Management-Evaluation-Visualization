<template>
  <div>
    <el-row class="checkscope-container">
      <!-- flex容器可以对各大浏览器进行兼容 -->
      <el-col :lg="6" :md="12" class="left">
        <div class="empty-line"></div>
        <div class="content-title">学医景商评价</div>
        <div class="empty-line"></div>
        <hr class="line" />
        <div class="empty-line"></div>
        <div class="showabout" style="font-size: 18px">
          <el-icon style="font-size: 30px">
            <ChatDotSquare />
          </el-icon>&nbsp;&nbsp;参数设置
        </div>
        <div class="showabout">
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;此站点仅支持[学]的数据查看
        </div>
        <div class="empty-line"></div>
        <hr class="line" />

        <!--<div id="xyjs" v-show="showUl">
          <div class="optionpart">
            <div class="bt">类型选择：</div>

            <div style="font-size: 17px;">

              <input type="checkbox" id="dwqk1" v-model="selectedOptions[0]" @change="checkscope"
                @click="lastClicked = 'dwqk1'" /> 学
              <input type="checkbox" id="dwqk2" v-model="selectedOptions[1]" @change="checkscope"
                @click="lastClicked = 'dwqk2'" /> 医
              <input type="checkbox" id="dwqk3" v-model="selectedOptions[2]" @change="checkscope"
                @click="lastClicked = 'dwqk3'" /> 景
              <input type="checkbox" id="dwqk4" v-model="selectedOptions[3]" @change="checkscope"
                @click="lastClicked = 'dwqk4'" /> 商
            </div>

          </div>
        </div>-->
        <div class="empty-line"></div>
        <!-- 行政区划标题 -->
        <div class="bt">行政区划：</div>

        <!-- 复选框组 -->
        <div class="flex flex-wrap ml-5 text-light-50">
          <div class="w-1/3 mb-2 flex">
            <input type="checkbox" name="qyxz" value="东城" v-model="selectedRegions" @change="handleRegionChange" />
            东城区
          </div>
          <div class="w-1/3 mb-2 flex">
            <input type="checkbox" name="qyxz" value="西城" v-model="selectedRegions" @change="handleRegionChange" />
            西城区
          </div>
          <div class="w-1/3 mb-2 flex">
            <input type="checkbox" name="qyxz" value="朝阳" v-model="selectedRegions" @change="handleRegionChange" />
            朝阳区
          </div>
          <div class="w-1/3 mb-2 flex">
            <input type="checkbox" name="qyxz" value="海淀" v-model="selectedRegions" @change="handleRegionChange" />
            海淀区
          </div>
          <div class="w-1/3 mb-2 flex">
            <input type="checkbox" name="qyxz" value="丰台" v-model="selectedRegions" @change="handleRegionChange" />
            丰台区
          </div>
          <div class="w-1/3 mb-2 flex">
            <input type="checkbox" name="qyxz" value="石景山" v-model="selectedRegions" @change="handleRegionChange" />
            石景山区
          </div>
          <div class="w-1/3 mb-2 flex">
            <input type="checkbox" name="qyxz" value="通州" v-model="selectedRegions" @change="handleRegionChange" />
            通州区
          </div>
          <div class="w-1/3 mb-2 flex">
            <input type="checkbox" name="qyxz" value="开发" v-model="selectedRegions" @change="handleRegionChange" />
            开发区
          </div>
          <div class="w-1/3 mb-2 flex">
            <input type="checkbox" name="qyxz" value="房山" v-model="selectedRegions" @change="handleRegionChange" />
            房山区
          </div>
          <div class="w-1/3 mb-2 flex">
            <input type="checkbox" name="qyxz" value="顺义" v-model="selectedRegions" @change="handleRegionChange" />
            顺义区
          </div>
          <div class="w-1/3 mb-2 flex">
            <input type="checkbox" name="qyxz" value="昌平" v-model="selectedRegions" @change="handleRegionChange" />
            昌平区
          </div>
          <div class="w-1/3 mb-2 flex">
            <input type="checkbox" name="qyxz" value="门头沟" v-model="selectedRegions" @change="handleRegionChange" />
            门头沟区
          </div>
          <div class="w-1/3 mb-2 flex">
            <input type="checkbox" name="qyxz" value="大兴" v-model="selectedRegions" @change="handleRegionChange" />
            大兴区
          </div>
          <div class="w-1/3 mb-2 flex">
            <input type="checkbox" name="qyxz" value="怀柔" v-model="selectedRegions" @change="handleRegionChange" />
            怀柔区
          </div>
          <div class="w-1/3 mb-2 flex">
            <input type="checkbox" name="qyxz" value="平谷" v-model="selectedRegions" @change="handleRegionChange" />
            平谷区
          </div>
          <div class="w-1/3 mb-2 flex">
            <input type="checkbox" name="qyxz" value="密云" v-model="selectedRegions" @change="handleRegionChange" />
            密云区
          </div>
          <div class="w-1/3 mb-2 flex">
            <input type="checkbox" name="qyxz" value="延庆" v-model="selectedRegions" @change="handleRegionChange" />
            延庆区
          </div>
        </div>
        <br />
        <div class="empty-line"></div>
        <div class="bt">点位选择：</div>
        <el-select v-model="selectedPoint" class="w-80 ml-5 my-custom-select" placeholder="请选择点位"
          @change="handleDropdownChange" :placement="'bottom'">
          <el-option v-for="point in pointsList" :key="point" :label="point" :value="point">
          </el-option>a
        </el-select>

        <el-button type="primary" style="margin-left: 95px; margin-top: 22px" @click="drawer = true">
          "学"数据维护
        </el-button>

        <el-drawer v-model="drawer" title="欢迎进行'学'数据维护" :direction="direction" :before-close="handleClose" size="65%"
          class="drawer-container">
          <div class="drawer-content">
            <div class="left-content">
              <div class="section-bigheader" style="margin-top: 0px">
                图片查看与删除
              </div>
              <div class="section-header">选择学校</div>
              <el-radio-group v-model="selectedSchoolForImages" size="middle" @change="loadSchoolImages"
                style="margin-bottom: 10px">
                <el-radio-button label="北京市东城区板厂小学低部校区" value="北京市东城区板厂小学低部校区" />
                <el-radio-button label="翠微小学南校区" value="翠微小学南校区" />
              </el-radio-group>
              <div class="image-gallery">
                <div class="image-container" v-for="image in schoolImages" :key="image.id">
                  <img :src="image.url" alt="学校图片" />
                  <el-button type="text" class="delete-button" @click="removeImage(image.id)">删除</el-button>
                </div>
              </div>

            </div>
            <div class="divider"></div>
            <div class="right-content">
              <div class="section-bigheader" style="margin-top: 0px">
                图片上传
              </div>
              <div class="section-header" style="margin-top: 0px">学校名称</div>
              <el-select v-model="selectedSchool" placeholder="请选择学校">
                <el-option label="北京市东城区板厂小学低部校区" value="北京市东城区板厂小学低部校区"></el-option>
                <el-option label="翠微小学南校区" value="翠微小学南校区"></el-option>
              </el-select>
              <div class="section-header">上传图片</div>
              <input type="file" @change="handleFileChange" ref="fileInput" style="display: none" />
              <el-button type="success" @click="clickFileInput">选择图片</el-button>
              <img :src="previewImage" alt="图片预览" v-if="previewImage" class="image-preview" />
              <el-button type="primary" @click="uploadImage">确认上传</el-button>
            </div>

          </div>
        </el-drawer>
      </el-col>

      <el-col :lg="18" :md="12" class="middle">
        <div id="baiduMap" style="width: 100%; height: 100%"></div>
      </el-col>

      <el-col :lg="6" :md="12" class="right">
        <div v-if="showTotalScore" ref="totalScoreContainer" style="width: 100%; overflow-y: auto; overflow-x: hidden">
        </div>
        <div v-else ref="visualizationContainer" style="width: 100%; height: 100%">
          <div ref="pieContainer" class="chart"></div>
          <div ref="barContainer" class="chart"></div>
          <div ref="radarContainer" class="chart"></div>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<!-- 单文件组件中使用组合式API的编译时语法糖 -->
<script setup>
import { ref, reactive, onMounted } from "vue";
import { ElNotification } from "element-plus";
import { ElMessage } from 'element-plus';
import { ElButton, ElIcon } from 'element-plus';
import { useRouter } from "vue-router";
import { Initial } from "~/network/home";
import { Region, Detail } from "~/network/home";
import { ImageCreate } from "~/network/home";
import { getIdList } from "~/network/home";
import { searchImage } from "~/network/home";
import { deleteImage } from "~/network/home";
import * as echarts from "echarts";
const router = useRouter();
const drawer = ref(false);
const direction = ref("rtl");
const radio1 = ref('New York')
</script>

<script>
export default {
  data() {
    return {
      schoolImages: [], // 存储加载的学校图片
      selectedSchoolForImages: null, // 用于图片查看功能的选择的学校
      selectedSchool: null, // 用于图片增加选择的学校
      showTotalScore: true, //右侧可视化容器切换显示
      showUl: true,
      selectAll: false,
      selectedOptions: [true, false, false, false], // 对应 "学", "医", "景", "商"
      lastClicked: "",
      selectedType: "学", // 默认选择“学”
      mapData: [], //存储从后端获取的数据
      map: null, //地图实例
      selectedPoint: null,
      pointsList: [], // 当前显示的点位名称，基于选中的行政区位
      locationToPointMap: {}, // 存储从后端获取的所有点位数据,用于处理映射关系
      selectedRegions: [], //存储所选的行政区域
      containerHeight: "auto", // 容器高度初始值
      selectedFile: null, //用于存储所选择要上传的文件发送给后端
      previewImage: null, //用于存储预览图片
    };
  },

  mounted() {
    //在组件挂载后初始化地图
    // 确保百度地图API已加载
    if (typeof BMap !== "undefined") {
      // 创建地图实例
      this.map = new BMap.Map("baiduMap");
      // 创建点坐标
      const point = new BMap.Point(116.404, 39.915);
      // 初始化地图，设置中心点坐标和地图级别
      this.map.centerAndZoom(point, 15);
      //开启鼠标滚轮缩放
      this.map.enableScrollWheelZoom(true);
      //设置地图样式
      this.map.setMapStyleV2({
        styleId: "43759cae3f2285df7123bee31e890767",
      });
      //从后端获取数据并绘制到地图上
      // this.fetchData();
      this.$nextTick(() => {
        this.fetchData();
      });
      // this.plotDataOnMap();
    } else {
      console.error("Baidu Map API not loaded");
    }
    // this.testforvisualization();
    // this.testQueryAPI('北京市第五十中学分校');  // 后端接口数据测试
    // 在适当的位置调用上述函数进行渲染
    // this.$nextTick(() => {
    this.testforvisualization1();
    // this.testforvisualization();
    // });
  },

  methods: {
    //“学医景商”复选框选择规则
    checkscope() {
      // 如果最后点击的是全选复选框
      if (this.lastClicked === "all") {
        // 如果全选复选框被选中
        if (this.selectAll) {
          // 选中所有其他复选框
          this.selectedOptions = [true, true, true, true];
        } else {
          // 否则，取消所有其他复选框的选择
          this.selectedOptions = [false, false, false, false];
        }
      } else {
        // 如果最后点击的是其他复选框
        // 检查是否有复选框未被选中
        if (this.selectedOptions.some((opt) => !opt)) {
          // 如果有未被选中的复选框，取消全选复选框的选择
          this.selectAll = false;
        } else {
          // 否则，选中全选复选框
          this.selectAll = true;
        }
      }
    },

    // handleClose(){
    //   ElMessageBox.confirm('Are you sure you want to close this?')
    //     .then(() => {
    //       done()
    //     })
    //     .catch(() => {
    //       // catch error
    //     })
    // },

    //聚焦所选择点位，缩放界面
    adjustMapView(point) {
      //将地图的中心移动到点位并设置缩放级别为18
      this.map.centerAndZoom(point, 18);
    },

    //处理选择点位下拉框change事件处理函数：聚焦点位、显示点位信息、展示点位详细数据
    handleDropdownChange() {
      //从下拉框中获取选择的点位名称
      const selectedPoint = this.selectedPoint;
      //获取该点位的坐标
      const point_selected = this.locationToPointMap[selectedPoint];
      this.adjustMapView(point_selected);
      //选择下拉框点位后获取详细数据并渲染可视化图形
      this.fetchAndRenderDetailVisualization(this.selectedPoint);
    },

    //异步操作从后端获取全部点位数据：将数据绘制到地图上显示所有点位、展示所有点位总评数据
    async fetchData() {
      //使用async/await进行异步操作
      try {
        this.showTotalScore = true;
        console.log("showTotalScore value:", this.showTotalScore);
        const response = await Initial(); //调用接口函数获取数据
        if (response.data) {
          this.mapData = response.data; //存储获取到的数据
          this.pointsList = response.data.map((item) => item.location);
          console.log(this.mapData);
          this.plotDataOnMap(this.mapData); //将数据绘制到地图上

          this.renderVisualization(this.mapData);

        }
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    },

    //可复用函数，在地图上描绘数据返回的点位
    plotDataOnMap(data) {
      //清除地图上的所有标记
      this.map.clearOverlays();
      console.log("aaa");
      if (!this.map) {
        console.error("Map is not initialized yet!");
        return;
      }
      const self = this;
      const myGeo = new BMap.Geocoder();
      const points = [];

      let delay = 0; // 初始化延迟为0

      data.forEach((item) => {
        delay += 34; // 递增延迟

        setTimeout(() => {
          // 使用 setTimeout 设置延迟
          myGeo.getPoint(item.location, function (point) {
            if (point) {
              self.locationToPointMap[item.location] = point; //将每个点保存到映射对象中
              points.push(point);
              const marker = new BMap.Marker(point);
              self.map.addOverlay(marker);

              //绑定点击事件
              marker.addEventListener("click", function () {
                self.showInfoWindow(item, point);
              });
            }
          });
        }, delay); // 在这里使用递增的延迟
      });
      self.map.setViewport(points);
    },

    //可复用函数，在地图上点击点位后显示信息窗口、展示所选择点位详细数据可视化
    showInfoWindow(item, point) {
      const content = `<div class=" background-color: #eef2ff;border-radius: 15px;padding: 10px;width: calc(1cm + 100px);height: calc(1cm + 50px);">
        学校名称: ${item.location}
        <br>
        评分: ${item.sum}
        </div>`;
      const infoWindow = new BMap.InfoWindow(content);
      this.map.openInfoWindow(infoWindow, point);
      this.adjustMapView(point);
      // 在点击地图标记后获取详细数据并渲染可视化图形
      this.fetchAndRenderDetailVisualization(item.location);
    },

    //异步操作：选择行政区划后自动更新：点位选择下拉框数据、地图点位重新绘制
    async handleRegionChange() {
      try {
        this.map.clearOverlays();
        let allData = []; //用于存储所有选中区域的数据

        for (let region of this.selectedRegions) {
          //对每个区域单独发送请求
          const response = await Region({ region: region });
          if (response && response.data) {
            //更新地图标记点
            this.plotDataOnMap(response.data);
            allData.push(...response.data); //将当前区域的数据添加到allData数组中
          }
        }

        this.pointsList = allData.map((item) => item.location);
        console.log(allData);
        this.renderVisualization2(allData); //使用allData数组更新可视化图表
      } catch (error) {
        // 如果在上述过程中出现任何错误，这里会捕获它，并在控制台上显示一个错误消息。
        console.error("Error fetching data based on regions:", error);
      }
    },

    //获取数据可视化-全局预览显示总评
    renderVisualization(data) {
      this.showTotalScore = true;
      const dataLength = data.length;
      const itemHeight = 40; //每个数据点的高度（包括间距）
      const chartHeight = dataLength * itemHeight;
      this.containerHeight = `${dataLength * itemHeight}px`;
      const container = this.$refs.totalScoreContainer;
      container.style.height = `${chartHeight}px`;
      const chart = echarts.init(container);

      console.log("showTotalScore value:", this.showTotalScore);

      const option = {
        title: {
          text: "评分显示", // 标题文本内容
          textStyle: {
            // 标题文本样式配置
            color: "#fafaf9", // 文本颜色
            fontSize: 18, // 字体大小
          },
          padding: [20, 10, 10, 10], // 标题内边距，可以设置为上右下左的数组形式，例如：[5, 10, 5, 10]
          left: "center", // 标题水平对齐方式，可以是'left'、'center'或'right'
          top: "top", // 标题垂直对齐方式，可以是'top'、'middle'或'bottom'
        },

        xAxis: {
          type: "value",
          splitLine: {
            show: false, // 隐藏X轴的分割线
          },
          axisLine: {
            show: false, // 隐藏X轴线
          },
          axisLabel: {
            show: false, // 隐藏X轴上的标签数据
          },
        },

        yAxis: {
          type: "category",
          data: data.map((item) => item.location),
          axisLabel: {
            fontSize: 13,
            color: "#fafaf9",
            formatter: function (value) {
              // 设置每行显示的最大字符数
              const maxLength = 7;
              let str = "";
              for (let i = 0; i < value.length; i++) {
                str += value[i];
                if (i !== 0 && i % maxLength === 0) {
                  str += "\n";
                }
              }
              return "{lineHeight|" + str + "}";
            },
            rich: {
              lineHeight: {
                lineHeight: 15, // 调整行间距的大小，单位为像素
              },
            },
          },
          splitLine: {
            show: false, // 隐藏Y轴的分割线
          },
          axisLine: {
            show: false, // 隐藏Y轴线
          },
        },
        series: [
          {
            data: data.map((item) => item.sum),
            type: "bar",
            barWidth: 10,
            barCategoryGap: "10%",
            // barCategoryGap: '100%',
            itemStyle: {
              color: "#34d399", //柱状颜色
              borderRadius: [10, 10, 10, 10],
            },
            emphasis: {
              //高亮状态下的样式
              itemStyle: {
                shadowBlur: 10, // 阴影的大小
                shadowOffsetX: 0, // 阴影水平方向上的偏移
                shadowColor: "rgba(0, 0, 0, 0.5)", // 阴影颜色
              },
            },
          },
        ],

        grid: {
          left: "40%", // 调整左边距
          right: "5%", // 调整右边距，可以根据需要进一步减少X轴的长度
          top: "50px", // 根据需要调整上边距
          bottom: "50px", // 根据需要调整下边距
        },

        tooltip: {
          trigger: "axis",
          position: function (point, params, dom, rect, size) {
            // 获取容器宽度和高度
            var containerWidth = size.viewSize[0];
            var containerHeight = size.viewSize[1];

            // 提示框宽度和高度
            var tooltipWidth = size.contentSize[0];
            var tooltipHeight = size.contentSize[1];

            // 计算最佳位置
            var x =
              point[0] + tooltipWidth > containerWidth
                ? point[0] - tooltipWidth
                : point[0];
            var y =
              point[1] + tooltipHeight > containerHeight
                ? point[1] - tooltipHeight
                : point[1];

            return [x, y];
          },
        },
      };

      chart.setOption(option);
    },

    renderVisualization2(data) {
      this.showTotalScore = true;
      const dataLength = data.length;
      const itemHeight = 60; // 每个数据点的高度（包括间距）
      const chartHeight = dataLength * itemHeight;
      const container = this.$refs.totalScoreContainer;
      container.style.height = "100%";
      // 清空容器内容
      container.innerHTML = "";
      const innerContent = document.createElement("div");
      innerContent.style.height = `${chartHeight}px`;
      container.appendChild(innerContent);
      const chart = echarts.init(innerContent);

      const option = {
        title: {
          text: "评分显示", // 标题文本内容
          textStyle: {
            // 标题文本样式配置
            color: "#fafaf9", // 文本颜色
            fontSize: 18, // 字体大小
          },
          padding: [20, 10, 10, 10], // 标题内边距，可以设置为上右下左的数组形式，例如：[5, 10, 5, 10]
          left: "center", // 标题水平对齐方式，可以是'left'、'center'或'right'
          top: "top", // 标题垂直对齐方式，可以是'top'、'middle'或'bottom'
        },

        xAxis: {
          type: "value",
          splitLine: {
            show: false, // 隐藏X轴的分割线
          },
          axisLine: {
            show: false, // 隐藏X轴线
          },
          axisLabel: {
            show: false, // 隐藏X轴上的标签数据
          },
        },

        yAxis: {
          type: "category",
          data: data.map((item) => item.location),
          axisLabel: {
            fontSize: 13,
            color: "#fafaf9",
            formatter: function (value) {
              // 设置每行显示的最大字符数
              const maxLength = 7;
              let str = "";
              for (let i = 0; i < value.length; i++) {
                str += value[i];
                if (i !== 0 && i % maxLength === 0) {
                  str += "\n";
                }
              }
              return "{lineHeight|" + str + "}";
            },
            rich: {
              lineHeight: {
                lineHeight: 15, // 调整行间距的大小，单位为像素
              },
            },
          },
          splitLine: {
            show: false, // 隐藏Y轴的分割线
          },
          axisLine: {
            show: false, // 隐藏Y轴线
          },
        },
        series: [
          {
            data: data.map((item) => item.sum),
            type: "bar",
            barWidth: 10,
            barCategoryGap: "10%",
            // barCategoryGap: '100%',
            itemStyle: {
              color: "#34d399", //柱状颜色
              borderRadius: [10, 10, 10, 10],
            },
            emphasis: {
              //高亮状态下的样式
              itemStyle: {
                shadowBlur: 10, // 阴影的大小
                shadowOffsetX: 0, // 阴影水平方向上的偏移
                shadowColor: "rgba(0, 0, 0, 0.5)", // 阴影颜色
              },
            },
          },
        ],

        grid: {
          left: "40%", // 调整左边距
          right: "5%", // 调整右边距，可以根据需要进一步减少X轴的长度
          top: "50px", // 根据需要调整上边距
          bottom: "50px", // 根据需要调整下边距
        },

        tooltip: {
          trigger: "axis",
          position: function (point, params, dom, rect, size) {
            // 获取容器宽度和高度
            var containerWidth = size.viewSize[0];
            var containerHeight = size.viewSize[1];

            // 提示框宽度和高度
            var tooltipWidth = size.contentSize[0];
            var tooltipHeight = size.contentSize[1];

            // 计算最佳位置
            var x =
              point[0] + tooltipWidth > containerWidth
                ? point[0] - tooltipWidth
                : point[0];
            var y =
              point[1] + tooltipHeight > containerHeight
                ? point[1] - tooltipHeight
                : point[1];

            return [x, y];
          },
        },
      };

      chart.setOption(option);
    },

    // 获取数据可视化-当点击地图标记或下拉框选择点位时，获取详细数据并渲染可视化图形
    async fetchAndRenderDetailVisualization(locationName) {
      try {
        // this.showTotalScore=false;
        const response = await Detail({ location: locationName });
        if (response && response.data) {
          this.showTotalScore = false;
          // 渲染三个可视化图形
          this.$nextTick(() => {
            this.renderPieChart(response.data);
            this.renderRadarChart(response.data);
            this.renderBarChart(response.data);
          });
          console.log("success!");
        }
      } catch (error) {
        console.error(
          "Error fetching detail data and rendering visualization:",
          error
        );
      }
    },

    //可复用函数，饼图函数
    renderPieChart(data) {
      const pieData = [
        { value: data.ti, name: "交通指数" },
        { value: data.im, name: "内部措施评分" },
        { value: data.to, name: "交通秩序评分" },
        { value: data.rs, name: "道路交通安全设施评分" },
        { value: data.sr, name: "满意度调查" },
      ];

      const option = {
        title: {
          text: "详细评分", // 标题文本内容
          textStyle: {
            // 标题文本样式配置
            color: "#fafaf9", // 文本颜色
            fontSize: 15, // 字体大小
          },
          padding: [10, 10, 10, 10], // 标题内边距，可以设置为上右下左的数组形式，例如：[5, 10, 5, 10]
          left: "center", // 标题水平对齐方式，可以是'left'、'center'或'right'
          top: "top", // 标题垂直对齐方式，可以是'top'、'middle'或'bottom'
        },

        tooltip: {
          show: true,
          confine: false, // 这使得tooltip不受容器限制
          trigger: "item",
          position: function (point, params, dom, rect, size) {
            // 获取容器宽度和高度
            var containerWidth = size.viewSize[0];
            var containerHeight = size.viewSize[1];

            // 提示框宽度和高度
            var tooltipWidth = size.contentSize[0];
            var tooltipHeight = size.contentSize[1];

            // 计算最佳位置
            var x =
              point[0] + tooltipWidth > containerWidth
                ? point[0] - tooltipWidth
                : point[0];
            var y =
              point[1] + tooltipHeight > containerHeight
                ? point[1] - tooltipHeight
                : point[1];

            return [x, y];
          },
        },

        series: [
          {
            name: "评分",
            type: "pie",
            data: pieData,
            radius: "50%", // 饼图的半径
            center: ["50%", "50%"], // 饼图的中心位置
            label: {
              show: true,
              formatter: "{b} ({c})", // 显示名称和百分比
              fontSize: 11,
            },
            emphasis: {
              label: {
                show: true,
                fontSize: 14,
              },
              tooltip: {
                show: true,
                formatter: "{a} ({d}%)", // {a} 为系列名称，{b} 为数据项名称，{c} 为数值，{d} 为百分比
                confine: false, // 这使得tooltip不受容器限制
              },
            },
          },
        ],
        legend: {
          type: "scroll", // 滚动式图例
          bottom: 3,
          data: pieData.map((item) => item.name),
        },
      };

      const container = this.$refs.pieContainer;
      const chart = echarts.init(container);
      // const chart = echarts.init(document.getElementById('pieContainer'));
      chart.setOption(option);
      console.log("333");
    },

    //可复用函数，雷达图函数
    renderRadarChart(data) {
      const radarData = [
        {
          value: [data.im1, data.im2, data.im3, data.im4, data.im5],
          name: "内部措施评分细分",
        },
      ];

      function ellipsisText(text, maxLength) {
        if (text.length > maxLength) {
          return text.substr(0, maxLength) + "...";
        }
        return text;
      }

      const indicatorData = [
        { name: ellipsisText("采取错峰上下学", 5), max: 2 },
        { name: ellipsisText("对学生及家长开展交通文明教育", 5), max: 2 },
        { name: ellipsisText("教育学生不乘坐违法电动二三四轮车", 5), max: 2 },
        { name: ellipsisText("制定“一校一策”工作方案", 5), max: 2 },
        { name: ellipsisText("新学期就交通安全致家长一封信", 5), max: 2 },
      ];
      const dicatorData = [
        { name: "采取错峰上下学", max: 2 },
        { name: "对学生及家长开展交通文明教育", max: 2 },
        { name: "教育学生不乘坐违法电动二三四轮车", max: 2 },
        { name: "制定“一校一策”工作方案", max: 2 },
        { name: "新学期就交通安全致家长一封信", max: 2 },
      ];

      const option = {
        radar: {
          indicator: indicatorData,
          shape: "polygon",
          radius: "70%",
          name: {
            textStyle: {
              color: "#fff",
            },
          },
        },
        tooltip: {
          trigger: "item",
          show: true,
          confine: false, // 这使得tooltip不受容器限制
          formatter: function (params) {
            let result = params.seriesName + "<br/>";
            params.value.forEach((value, index) => {
              result += dicatorData[index].name + ": " + value + "<br/>";
            });
            return result;
          },
          // backgroundColor: 'rgba(0,0,0,0.7)',  // 黑色背景
          borderColor: "#475569", // 边框颜色
          borderWidth: 1, // 边框宽度
          padding: 10, // 内边距
          textStyle: {
            fontSize: 8, // 调整字体大小
          },
          position: function (point, params, dom, rect, size) {
            var offset = 20;
            var left = point[0] - size.contentSize[0] / 2 - 10; // 设置左边距
            var right = "auto"; // 设置右边距
            var top = point[1] - size.contentSize[1] - 10 - offset;
            return [left, top, right];
          },
        },

        series: [
          {
            name: "内部措施评分细分",
            type: "radar",
            data: radarData,
          },
        ],
        legend: {
          type: "scroll",
          bottom: 0,
          data: ["内部措施评分细分"],
        },
      };
      const container = this.$refs.radarContainer;
      const chart = echarts.init(container);
      // const chart = echarts.init(document.getElementById('radarContainer'));
      chart.setOption(option);
    },

    //可复用函数，柱状图函数
    renderBarChart(data) {
      const barData = [
        { value: data.to1, name: "四支队伍建设" },
        { value: data.to2, name: "机动车停车秩序" },
        { value: data.to3, name: "非机动车停车秩序" },
        { value: data.to4, name: "行人秩序" },
        { value: data.to5, name: "文明出行" },
      ];

      const option = {
        yAxis: {
          type: "category",
          data: barData.map((item) => item.name),
          axisLabel: {
            fontSize: 12,
            color: "#fafaf9",
          },
        },
        xAxis: {
          type: "value",
        },
        series: [
          {
            data: barData.map((item) => item.value),
            type: "bar",
            barWidth: 10,
            itemStyle: {
              color: "#34d399", //柱状颜色
              borderRadius: [5, 5, 5, 5],
            },
          },
        ],
        tooltip: {
          trigger: "axis",
          axisPointer: {
            type: "shadow",
          },
        },
        legend: {
          type: "scroll",
          bottom: 5,
          data: ["to1", "to2", "to3", "to4", "to5"],
        },

        grid: {
          left: "36%", // 调整左边距
          right: "5%", // 调整右边距，可以根据需要进一步减少X轴的长度
          top: "5px", // 根据需要调整上边距
          bottom: "5px", // 根据需要调整下边距
        },
      };

      const container = this.$refs.barContainer;
      const chart = echarts.init(container);
      // const chart = echarts.init(document.getElementById('barContainer'));
      chart.setOption(option);
      console.log("111");
    },

    //总评信息测试数据
    testforvisualization() {
      console.log("aaa");
      const mockData = [
        { location: "东城区第一小学第一小学第一小学", sum: 85 },
        { location: "西城区", sum: 90 },
        { location: "海淀区", sum: 95 },
        { location: "丰台区", sum: 78 },
        { location: "海淀区", sum: 95 },
        { location: "西城区", sum: 90 },
        { location: "朝阳区", sum: 88 },
        { location: "房山区", sum: 79 },
      ];
      this.renderVisualization(mockData);
    },
    //详细信息测试数据
    testforvisualization1() {
      console.log("aaaa");
      const mockData = {
        ti: 85,
        im: 88,
        to: 80,
        rs: 82,
        sr: 79,
        to1: 80,
        to2: 85,
        to3: 78,
        to4: 88,
        to5: 82,
        im1: 1.8,
        im2: 1.6,
        im3: 1.5,
        im4: 1.9,
        im5: 1.7,
      };

      this.showTotalScore = false;
      this.$nextTick(() => {
        this.renderPieChart(mockData);
        this.renderRadarChart(mockData);
        this.renderBarChart(mockData);
      });
    },

    //上传图片文件函数
    clickFileInput() {
      this.$refs.fileInput.click(); // 触发文件选择器，允许用户选择文件。
    },
    handleFileChange(event) {
      this.selectedFile = event.target.files[0]; // 获取用户选择的文件并保存到 selectedFile 变量中。
      // 预览图片
      if (this.selectedFile) {
        this.previewImage = URL.createObjectURL(this.selectedFile); // 如果选择了文件，则创建一个预览 URL 并保存到 previewImage 变量中。
      } else {
        this.previewImage = null; // 如果没有选择文件，则清除预览 URL。
      }
    },
    uploadImage() {
      if (!this.selectedSchool) {
        console.log("未选择学校");
        return;
      }
      const params = {
        name: this.selectedSchool, // 使用选择的学校名称
        image_file: this.selectedFile // 选择的图片文件
      };

      ImageCreate(params).then(response => {
        if (response.data && response.data.length > 0) {
          // 获取 image_id 值
          // const imageId = response.data[0].image_id;

          // 成功上传图片，弹出成功提示
          this.$message.success('图片上传成功!');

          // 清除预览图片
          this.previewImage = null;
          this.selectedFile = null;
        } else if (response.errs) {

          // 弹出错误提示
          this.$message.error('上传失败: ' + response.errs);
        }
      });
    },

    //查看选择学校的所有图片
    async loadSchoolImages() {
      const schoolName = this.selectedSchoolForImages; // 获取选择的学校名称
      console.log("Selected school:", schoolName); // 打印选择的学校名称

      // 获取图片ID列表
      const idListResponse = await getIdList({ name: schoolName });
      const ids = idListResponse.data;
      console.log("Received IDs:", ids); // 打印收到的ID列表

      // 初始化图片数组
      this.schoolImages = [];

      // 遍历ID列表，获取每张图片
      for (const id of ids) {
        console.log("Fetching image with ID:", id); // 打印当前处理的ID
        const imageResponse = await searchImage({ id });
        const imageUrl = URL.createObjectURL(new Blob([imageResponse]));
        this.schoolImages.push({ id, url: imageUrl });
        console.log("Image URL created:", imageUrl); // 打印创建的图片URL
      }

      console.log("All images loaded:", this.schoolImages); // 打印所有加载的图片
    },

    //删除特定图片
    async removeImage(imageId) {
      try {
        const response = await deleteImage({ id: imageId });
        if (response.info === "图片删除成功！") {
          console.log("Image deleted successfully.");
          // 显示成功通知
          ElMessage.success('图片删除成功！');
          // 重新加载所选择的学校的所有图片
          await this.loadSchoolImages();
        } else {
          // 图片删除失败，记录错误信息
          console.error("Image deletion failed:", response.info);
          // 你也可以选择在此处显示错误通知
          ElMessage.error('图片删除失败: ' + response.info);
        }
      } catch (error) {
        // 发生异常时记录错误
        console.error("An error occurred while deleting the image:", error);
      }
    },

  },
};
</script>

<style scoped>
.image-preview {
  width: 500px;
  height: auto;
  margin: 20px 0;
  /* 20px 上下边距 */
}

.drawer-container {
  display: flex;
  background-color: #f5f5f5;
}

.drawer-content {
  display: flex;
  width: 100%;
  background-color: white;
  border-radius: 10px;
  overflow: hidden;
}


.left-content {
  flex: 3;
  padding: 20px;
}

.right-content {
  flex: 2;
  padding: 20px;
}


.divider {
  width: 10px;
  background-color: #f5f5f5;
}

.section-bigheader {
  margin-top: 0px;
  margin-bottom: 10px;
  font-size: 20px;
  font-weight: bold;
  color: #203262;
}

.section-header {
  margin-top: 10px;
  margin-bottom: 10px;
  font-weight: bold;
  color: #606c7a;
}

.checkscope-container {
  @apply min-h-screen bg-slate-600;
}

.checkscope-container .middle {
  @apply flex items-center justify-center;
}

.checkscope-container .right {
  @apply flex justify-center;
  position: absolute;
  top: 0;
  right: 0;
  width: 25%;
  /* Adjust as needed */
  /* height: 100%; */
  height: 100vh;
  min-height: 100vh;
  /* max-height:2000px; */
  /* Assuming it takes the whole viewport height */
  background-color: hsl(215, 19%, 35%, 0.6);
  /* This gives a slight transparency */
  z-index: 0;

  overflow-y: auto;
  overflow-x: hidden;
}

.checkscope-container .middle {
  @apply bg-light-50 flex-col;
}

.optionpart {
  @apply flex items-center text-xl text-light-50;
  display: flex;
  gap: 4px;
}

input[type="checkbox"] {
  @apply w-5 h-5 text-blue-600 rounded-md border border-gray-400 focus: border-blue-500 focus:ring focus:ring-blue-200 focus:ring-opacity-50 mr-1;
}

.optionpart .lx {
  @apply flex items-center mb-2 ml-5 text-light-50 text-lg gap-6;
}

.left .bt {
  @apply flex items-center mt-3 mb-4 ml-5 text-light-50 text-lg;
  font-size: 18px;
}

.left .content-title {
  @apply font-bold text-2xl text-light-50 flex justify-center my-4 font-sans;
}

.showabout {
  @apply text-normal text-light-50 flex justify-right ml-2;
}

.line {
  @apply my-2 border-t border-gray-400;
}

.empty-line {
  margin-top: 18px;
  /* 上边距控制空行的高度 */
  margin-bottom: 18px;
  /* 下边距控制空行的高度 */
}

.custom-info-window {
  background-color: #eef2ff;
  border-radius: 15px;
  padding: 10px;
  width: calc(1cm + 100px);
  height: calc(1cm + 50px);
}

.my-custom-select {
  width: 270px;
  /* 调整宽度 */
  margin-left: 20px;
  /* 调整左边距 */
  /* 其他样式调整 */
}

/* #visualizationContainer {
  height: 100vh;
  /* max-height: 2000px; */
/* 根据您的实际需求调整 */
/* overflow-y: auto;
  overflow-x: hidden; */
/* }  */

.chart {
  height: 32%;
  margin: 1% 0;
}

.item {
  margin-bottom: 1px;
  /* 设置底部间距为10像素 */
}

.image-gallery {
  display: flex;
  flex-wrap: wrap;
  /* 允许多行 */
  gap: 16px;
  /* 设置图片之间的间距 */
}

.image-container {
  flex: 1 0 200px;
  /* 每张图片至少200px宽 */
  position: relative;
  /* 相对定位，使其内部的绝对定位元素正确定位 */
  display: inline-block;
  /* 使图片和按钮在同一个行内块中 */
}

.delete-button {
  position: absolute;
  /* 定位在图片上 */
  right: 10px;
  /* 从右边调整位置 */
  top: 10px;
  /* 从顶部调整位置 */
  border-radius: 15px;
  /* 圆角 */
  background-color: rgba(14, 165, 233, 0.8);
  /* 使用 #0ea5e9 颜色，透明度为 0.8 */
  color: white;
  /* 文字颜色 */
  padding: 5px 10px;
  /* 内边距 */
  font-size: 14px;
  /* 字体大小 */
}

.delete-button.el-button:active,
.delete-button.el-button:focus,
.delete-button.el-button:hover {
  background-color: rgba(14, 165, 233, 0.8);
  /* 保持 #0ea5e9 背景颜色，透明度为 0.8 */
  color: white;
  /* 保持文字颜色 */
}



.image-container {
  max-width: 90%;
  height: auto;
  /* 保持原始宽高比 */
}</style>
