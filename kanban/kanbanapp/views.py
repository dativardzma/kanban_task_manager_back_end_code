from django.shortcuts import render
from .serializers import TableSerializer, BlogSerializer, SubTaskSerializer
from .models import Table, Blog, SubTask
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status

class TableView(ListCreateAPIView, RetrieveUpdateDestroyAPIView):
    serializer_class = TableSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        table = serializer.save()
        result = {
            "title": table.title,
            "message": 'Table succsefully created'
        }
        return Response(result, status=status.HTTP_201_CREATED)
    
    def delete(self, request, *args, **kwargs):
        table_id = kwargs.get('pk')
        try:
            table = Table.objects.get(id=table_id)
            table.delete()
            return Response({"message": "Table succsefully deleted"}, status=status.HTTP_200_OK)
        except Table.DoesNotExist:
            return Response({"error": "Table not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        table_id = kwargs.get('pk')
        try:
            table = Table.objects.get(id=table_id)
        except Table.DoesNotExist:
            return Response({"error": "Table not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = TableSerializer(table, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Table succsefully updated"}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        table_id = kwargs.get('pk')

        if table_id:
            try:
                table = Table.objects.get(id=table_id)
                serializer = TableSerializer(table)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Table.DoesNotExist:
                return Response({"error": "Table not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            tables = Table.objects.all()
            serializer = TableSerializer(tables, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)


class BlogView(ListCreateAPIView, RetrieveUpdateDestroyAPIView):
    serializer_class = BlogSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            table = serializer.validated_data['table']
            column = serializer.validated_data['status']

            if column not in table.columns:
                return Response({"error": f"Invalid column: {column}. Allowed: {table.columns}"}, status=status.HTTP_400_BAD_REQUEST)
            
            blog = serializer.save()
            result = {
                'message': "Blog succsefully created",
                'blog_name': blog.title,
                'blog_description': blog.description,
                'blog_in_table': blog.table.id,
                'blog_status': blog.status,
                'blog_subtasks': SubTaskSerializer(blog.subtasks.all(), many=True).data
            }
            return Response(result, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, *args, **kwargs):
        blog_id = kwargs.get('pk')
        try:
            blog = Blog.objects.get(id=blog_id)
            blog.delete()
            return Response({"message": "Blog succsefully deleted"}, status=status.HTTP_200_OK)
        except Blog.DoesNotExist:
            return Response({"error": "Blog not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        blog_id = kwargs.get('pk')
        try:
            blog = Blog.objects.get(id=blog_id)
        except Blog.DoesNotExist:
            return Response({"error": "Blog not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = BlogSerializer(blog, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Blog succsefully updated"}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        blog_id = kwargs.get('pk')

        if blog_id:
            try:
                blog = Blog.objects.get(id=blog_id)
                serializer = BlogSerializer(blog)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Blog.DoesNotExist:
                return Response({"error": "Blog not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            blogs = Blog.objects.all()
            serializer = BlogSerializer(blogs, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)    

class SubTaskView(ListCreateAPIView, RetrieveUpdateDestroyAPIView):
    serializer_class = SubTaskSerializer
    def post(self,request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        subtask = serializer.save(status="not ready")
        result = {
            'title': subtask.title,
            'description': subtask.description
        }
        return Response(result, status=status.HTTP_201_CREATED)

    def delete(self, request, *args, **kwargs):
        subtask_id = kwargs.get('pk')
        try:
            subtask = SubTask.objects.get(id=subtask_id)
            subtask.delete()
            return Response({"message": "Subtask succsefully deleted"}, status=status.HTTP_200_OK)
        except SubTask.DoesNotExist:
            return Response({"error": "Subtask not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        subtask_id = kwargs.get('pk')
        try:
            subtask = SubTask.objects.get(id=subtask_id)
        except SubTask.DoesNotExist:
            return Response({"error": "Subtask not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = SubTaskSerializer(subtask, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Subtask succsefully updated"}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        subtask_id = kwargs.get('pk')

        if subtask_id:
            try:
                subtask = SubTask.objects.get(id=subtask_id)
                serializer = SubTaskSerializer(subtask)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except SubTask.DoesNotExist:
                return Response({"error": "Subtask not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            subtasks = SubTask.objects.all()
            serializer = SubTaskSerializer(subtasks, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
