from django.db import models


class DataFormat(models.Model):
    name = models.CharField(max_length=10, unique=True, null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Data Format'
        verbose_name_plural = 'Data Format'


class DegreeOfAggregation(models.Model):
    name = models.CharField(max_length=100, blank=False, unique=True, null=False)
    description = models.TextField(blank=True, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Degree of Aggregation'
        verbose_name_plural = 'Degrees of Aggregation'


class ResearchMetadata(models.Model):
    data_provider = models.CharField(max_length=100, blank=False, null=False)
    data_format = models.ForeignKey(DataFormat, on_delete=models.PROTECT, related_name='research_metadata',
                                    null=False, blank=False)
    degree_of_aggregation = models.ForeignKey(DegreeOfAggregation, on_delete=models.PROTECT,
                                              related_name='research_metadata',
                                              null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.data_provider

    class Meta:
        verbose_name = 'Research Metadata'
        verbose_name_plural = 'Research Metadata'
        ordering = ['-created_at']
