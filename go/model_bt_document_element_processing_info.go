/*
 * Onshape REST API
 *
 * The Onshape REST API consumed by all clients.
 *
 * API version: 1.111
 * Contact: api-support@onshape.zendesk.com
 * Generated by: OpenAPI Generator (https://openapi-generator.tech)
 */

package openapi
// BtDocumentElementProcessingInfo struct for BtDocumentElementProcessingInfo
type BtDocumentElementProcessingInfo struct {
	AngleUnits string `json:"angleUnits,omitempty"`
	DataType string `json:"dataType,omitempty"`
	ElementType string `json:"elementType,omitempty"`
	Filename string `json:"filename,omitempty"`
	ForeignDataId string `json:"foreignDataId,omitempty"`
	Id string `json:"id,omitempty"`
	LengthUnits string `json:"lengthUnits,omitempty"`
	MassUnits string `json:"massUnits,omitempty"`
	MicroversionId string `json:"microversionId,omitempty"`
	Name string `json:"name,omitempty"`
	SpecifiedUnit string `json:"specifiedUnit,omitempty"`
	ThumbnailInfo BtThumbnailInfo `json:"thumbnailInfo,omitempty"`
	Thumbnails string `json:"thumbnails,omitempty"`
	TranslationEventKey string `json:"translationEventKey,omitempty"`
	TranslationId string `json:"translationId,omitempty"`
	Type string `json:"type,omitempty"`
	Unupdatable bool `json:"unupdatable,omitempty"`
}
